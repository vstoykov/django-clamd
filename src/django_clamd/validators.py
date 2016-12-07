import warnings

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django_clamd import get_scanner
from .conf import CLAMD_ENABLED


def validate_file_infection(file):
    # If django-clamd is disabled (for debugging) then do not check the file.
    if not CLAMD_ENABLED:
        warnings.warn('Runing clamd validator with CLAMD_ENABLED=False')
        return
    # Ensure file pointer is at begingin of the file
    file.seek(0)
    scanner = get_scanner()
    result = scanner.instream(file)
    if result and result['stream'][0] == 'FOUND':
        raise ValidationError(_('File is infected with malware.'), code='infected')
    # Return file pointer at initial state
    file.seek(0)
