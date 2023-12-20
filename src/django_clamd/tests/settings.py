import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


INSTALLED_APPS = [
    'django_clamd',
]

SECRET_KEY = 'Anti virus scanner'

LANGUAGE_CODE = 'en'

USE_TZ = True


CLAMD_USE_TCP = bool(os.getenv("CLAMD_USE_TCP") or False)
CLAMD_TCP_SOCKET = int(os.getenv("CLAMD_TCP_SOCKET") or 3310)
