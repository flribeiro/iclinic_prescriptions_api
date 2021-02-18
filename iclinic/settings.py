"""
Django settings for iclinic project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'prescriptions',
    'coverage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iclinic.urls'

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

WSGI_APPLICATION = 'iclinic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME", default='postgres'),
        'USER': env("DB_USER", default='postgres'),
        'PASSWORD': env("DB_PASSWD"),
        'HOST': env("DB_HOST", default='127.0.0.1'),
        'PORT': env("DB_PORT", default=5432),
        'TEST': {
            'NAME': 'test_db',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Cache system
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': env('REDIS_LOCATION'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logform': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'logform'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'iclinic_prescriptions.log',
            'formatter': 'logform'
        },
    },
    'loggers': {
        'prescriptions': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True
        },
    },
}

# ENV VARIABLES
ENV = {
    'physicians_api': {
        'key': env('PHYSICIANS_API_TOKEN'),
        'url': env('PHYSICIANS_API_URL'),
        'path': env('PHYSICIANS_API_PATH'),
        'timeout': env('PHYSICIANS_API_TIMEOUT'),
        'retry': env('PHYSICIANS_API_RETRY'),
        'cache_ttl': env('PHYSICIANS_API_CACHE_TTL_HOURS'),
    },
    'clinics_api': {
        'key': env('CLINICS_API_TOKEN'),
        'url': env('CLINICS_API_URL'),
        'path': env('CLINICS_API_PATH'),
        'timeout': env('CLINICS_API_TIMEOUT'),
        'retry': env('CLINICS_API_RETRY'),
        'cache_ttl': env('CLINICS_API_CACHE_TTL_HOURS'),
    },
    'patients_api': {
        'key': env('PATIENTS_API_TOKEN'),
        'url': env('PATIENTS_API_URL'),
        'path': env('PATIENTS_API_PATH'),
        'timeout': env('PATIENTS_API_TIMEOUT'),
        'retry': env('PATIENTS_API_RETRY'),
        'cache_ttl': env('PATIENTS_API_CACHE_TTL_HOURS'),
    },
    'metrics_api': {
        'key': env('METRICS_API_TOKEN'),
        'url': env('METRICS_API_URL'),
        'path': env('METRICS_API_PATH'),
        'timeout': env('METRICS_API_TIMEOUT'),
        'retry': env('METRICS_API_RETRY'),
    },
}
