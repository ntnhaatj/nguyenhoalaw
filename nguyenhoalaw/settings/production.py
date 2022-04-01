import os

from .base import *


SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY cannot be empty")

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
