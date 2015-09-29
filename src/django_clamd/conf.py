from django.conf import settings as _settings

# Default local socket for Debian based systems
# For Fedora you need to set CLAMD_SOCKET = '/var/run/clamd.scan/clamd.sock'
CLAMD_SOCKET = getattr(_settings, 'CLAMD_SOCKET', '/var/run/clamav/clamd.ctl')

# If you want to use TCP socket set this to True
CLAMD_USE_TCP = getattr(_settings, 'CLAMD_USE_TCP', False)

# Default ClamD TCP socket port
CLAMD_TCP_SOCKET = getattr(_settings, 'CLAMD_TCP_PORT', 3310)
# Default CLamd TCP socket addres
CLAMD_TCP_ADDR = getattr(_settings, 'CLAMD_TCP_SOCKET', '127.0.0.1')
