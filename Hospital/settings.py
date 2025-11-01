import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
DEBUG = False

ALLOWED_HOSTS = ['hms-gt67.onrender.com', 'localhost', '127.0.0.1']