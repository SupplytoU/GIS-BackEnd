import os
from ugavi.settings import *
from ugavi.settings import BASE_DIR                                                               

dotenv_file = BASE_DIR / '.env.production'
dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ.get('MY_SECRET_KEY')
if not SECRET_KEY:
    raise Exception('DJANGO_SECRET_KEY environment variable not defined')

DEBUG=False 

ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME')]     
if not ALLOWED_HOSTS or ALLOWED_HOSTS == ['']:
    raise Exception('DJANGO_ALLOWED_HOSTS environment variable not defined or empty') 
                                                               
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ.get('WEBSITE_HOSTNAME')]

# REDIRECT_URLS = os.environ.get('REDIRECT_URLS', '').split(',')
# if not REDIRECT_URLS or REDIRECT_URLS == ['']:
#     raise Exception('REDIRECT_URLS environment variable not defined or empty')

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 31536000  
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

AUTH_COOKIE_SECURE=True

CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
CONNECTION_STR = {pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CONNECTION_STR['dbname'],
        "HOST": CONNECTION_STR['host'],
        "USER": CONNECTION_STR['user'],
        "PASSWORD": CONNECTION_STR['password'],
    }
}                 