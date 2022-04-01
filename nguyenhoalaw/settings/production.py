import os

from .base import *


SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY cannot be empty")

DEBUG = False

# correct to use deployment env
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("HD_DB_NAME", "nguyenhoalaw"),
        'USER': os.environ.get("HD_DB_USER", "nguyenhoalaw"),
        'PASSWORD': os.environ.get("HD_DB_PASSWORD", "123456"),
        'HOST': os.environ.get("HD_DB_HOST"),
        'PORT': os.environ.get("HD_DB_PORT", "5432"),
    }
}

try:
    from .local import *
except ImportError:
    pass
