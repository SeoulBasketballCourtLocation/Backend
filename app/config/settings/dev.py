from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.dev.application'
