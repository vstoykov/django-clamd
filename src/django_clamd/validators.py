import re
import warnings
import logging

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django_clamd import get_scanner
from .conf import CLAMD_ENABLED, CLAMD_FAIL_BY_DEFAULT


logger = logging.getLogger(__name__)


def validate_file_infection(file):
    if file is None:
        return
    # If django-clamd is disabled (for debugging) then do not check the file.
    if not CLAMD_ENABLED:
        warnings.warn('Running clamd validator with CLAMD_ENABLED=False')
        return
    # Ensure file pointer is at begingin of the file
    file.seek(0)
    scanner = get_scanner()
    try:
        result = scanner.instream(file)
    except IOError:
        # Ping the server if it fails than the server is down
        scanner.ping()
        # Server is up. This means that the file is too big.
        logger.warning('The file is too large for ClamD to scan it. Bytes Read {}'.format(file.tell()))
        file.seek(0)
        if CLAMD_FAIL_BY_DEFAULT:
            raise ValidationError(
                _('Malware scan could not be completed. Please try again later.'),
                code='incomplete')
        return

    if result and result['stream'][0] == 'FOUND':
        # Check if the file was rejected by ClamD because it exceeded a config limit. If
        # so, log the reason and raise a ValidationError with a specific code.
        if match := re.match(r'^Heuristics\.Limits\.Exceeded(?:\.(\w+))?$', result['stream'][1]):
            reason = match.group(1) or 'unknown'
            logger.warning('The file was rejected by ClamD as it exceeded the "{}" config limit. Bytes Read {}'.format(reason, file.tell()))
            raise ValidationError(
                _('Malware scan could not be completed.'),
                code='limit_exceeded_{}'.format(reason.lower())
            )
        # Otherwise the file is infected with malware.
        raise ValidationError(_('File is infected with malware.'), code='infected')
    # Return file pointer at initial state
    file.seek(0)
