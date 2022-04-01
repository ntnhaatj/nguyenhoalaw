import os

from .base import *


SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY cannot be empty")

DEBUG = False

# correct to use deployment env
ALLOWED_HOSTS = ["*"]

try:
    from .local import *
except ImportError:
    pass
