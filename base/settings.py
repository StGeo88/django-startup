# -*- coding:utf-8 -*-
from os.path import join, dirname


BASE_DIR = dirname(dirname(__file__))
DEBUG = True  # SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']

if DEBUG:  # DEV settings.
    TEMPLATE_DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:  # DEPLOY settings.
    TEMPLATE_DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '477)6e=2+$21qe8)@w#bq=f1anv5ebxf)g+*cv7=__lt^)5c30'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'base.urls'

WSGI_APPLICATION = 'base.wsgi.application'


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    join(BASE_DIR, 'base/static'),
)


# Template files

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'base/templates'),
        ],
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


# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = join(BASE_DIR, "media")


# Auth (login)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


try:
    from local_settings import *
except Exception as e:
    pass
