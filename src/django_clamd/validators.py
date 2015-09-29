from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django_clamd import get_scanner


def validate_file_infection(file):
    # Ensure file pointer is at begingin of the file
    file.seek(0)
    scanner = get_scanner()
    result = scanner.instream(file)
    if result:
        raise ValidationError(_('File is infected with mallware'))
    # Return file pointer at initial state
    file.seek(0)
