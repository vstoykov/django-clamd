import warnings
import logging

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django_clamd import get_scanner
from .conf import CLAMD_ENABLED


logger = logging.getLogger(__name__)


def validate_file_infection(file):
    # If django-clamd is disabled (for debugging) then do not check the file.
    if not CLAMD_ENABLED:
        warnings.warn('Runing clamd validator with CLAMD_ENABLED=False')
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
        logger.warn('The file is too large for ClamD to scan it. Bytes Read {}'.format(file.tell()))
        file.seek(0)
        return

    if result and result['stream'][0] == 'FOUND':
        raise ValidationError(_('File is infected with malware.'), code='infected')
    # Return file pointer at initial state
    file.seek(0)
