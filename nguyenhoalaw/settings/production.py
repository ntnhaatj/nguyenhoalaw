import os

from .base import *


SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY cannot be empty")

DEBUG = True
WHITENOISE_AUTOREFRESH = False

# correct to use deployment env
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME", "nguyenhoalaw"),
        'USER': os.environ.get("DB_USER", "nguyenhoalaw"),
        'PASSWORD': os.environ.get("DB_PASSWORD", "123456"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT", "5432"),
    }
}

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

try:
    from .local import *
except ImportError:
    pass
