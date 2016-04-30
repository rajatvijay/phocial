"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Loing Login Constants
LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kj+083khx)hw(0olq$p#jk+d9s8j+7n$+qw-cun8(fgj@*2)1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Custom Authetication backened
AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'account.authentication.EmailAuthBackend',
  'social.backends.facebook.Facebook2OAuth2',
  'social.backends.twitter.TwitterOAuth',
)

ALLOWED_HOSTS = []

# Email backened
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Media 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Facebook Auth
SOCIAL_AUTH_FACEBOOK_KEY = '694153904068955' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '53e5f269b9d4fb3a357662f154720657' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Twitter Auth
SOCIAL_AUTH_TWITTER_KEY = 'i0GVS0HtoC02avhSYTQx4EktD' # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = 'qXMUlyg7cMYxkqkI41sPyjXTErlbji1VnRPZOkDFaU1g5DES2P' # Twitter Consumer Secret

# Google Auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1005072635891-f2i7micjqcaqc84721fptnrgd77hk903.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'FjoCwzaHQ20lmZkVIKmY6b6M' # Google Consumer Secret

THUMBNAIL_DEBUG = True


# Application definition

INSTALLED_APPS = (
    'account',
    'images',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'sorl.thumbnail',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'bookmarks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
