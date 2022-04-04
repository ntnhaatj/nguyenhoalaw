import os

from .base import *


SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY cannot be empty")

DEBUG = True

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

# using whitenoise for serving static files
MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# cloudinary storage for heroku deployment only for media files
INSTALLED_APPS += [
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get("CLOUDINARY_NAME", "foo"),
    'API_KEY': os.environ.get("CLOUDINARY_API_KEY", "foo"),
    'API_SECRET': os.environ.get("CLOUDINARY_API_SECRET", "foo"),
    'STATICFILES_MANIFEST_ROOT': os.path.join(BASE_DIR, "static")
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

try:
    from .local import *
except ImportError:
    pass
