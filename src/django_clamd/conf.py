import os
import warnings

from django.conf import settings as _settings


# File based socked of ClamD. If not provided we will guess.
CLAMD_SOCKET = getattr(_settings, 'CLAMD_SOCKET', None)

if CLAMD_SOCKET is None:
    # Socket is not configured. Lets guess.
    if os.path.exists('/var/run/clamd.scan/'):
        # Fedora, CentOS
        CLAMD_SOCKET = '/var/run/clamd.scan/clamd.sock'
    else:
        # This is default for Ubuntu, Debian based distributions
        CLAMD_SOCKET = '/var/run/clamav/clamd.ctl'

# If you want to use TCP socket set this to True
CLAMD_USE_TCP = getattr(_settings, 'CLAMD_USE_TCP', False)

# Default ClamD TCP socket port
CLAMD_TCP_SOCKET = getattr(_settings, 'CLAMD_TCP_SOCKET', 3310)
# Default CLamd TCP socket addres
CLAMD_TCP_ADDR = getattr(_settings, 'CLAMD_TCP_ADDR', '127.0.0.1')

# Enable ClamD scanner. By default True. Set to False only for development.
CLAMD_ENABLED = getattr(_settings, 'CLAMD_ENABLED', True)

if not _settings.DEBUG and not CLAMD_ENABLED:
    warnings.warn('You are running with DEBUG=False and CLAMD_ENABLED=False. This is probably due to missconfigurations.')
