import dj_database_url

from .common import *

SECRET_KEY = '4ln7qg*67amc&7-h^=^0%ml_s(w4y_fy4uybib%j(v(46-x0i2'
DEBUG = False
ALLOWED_HOSTS = ['*']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
