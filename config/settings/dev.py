import socket
from .base import *


DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8040",
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
