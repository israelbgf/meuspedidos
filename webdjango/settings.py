"""
Django settings for webdjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'zpye1s(h9tqjq083=euo(aw4ctlvj129^cwn3g8bixaiqn-o0c'

DEBUG = True
TEMPLATE_DEBUG = False

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'webdjango', 'templates'),)
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'webdjango'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'webdjango.urls'
WSGI_APPLICATION = 'webdjango.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

EMAIL_HOST = os.environ.get('MAIL_SERVER', 'localhost')
EMAIL_PORT = int(os.environ.get('MAIL_PORT', 1025))
EMAIL_HOST_USER = os.environ.get('MAIL_USERNAME', '')
EMAIL_HOST_PASSWORD = os.environ.get('MAIL_PASSWORD', '')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}