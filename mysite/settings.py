"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import requests

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')=='1'

# SECURITY WARNING: keep the secret key used in production secret!
#DEV_SECRET_KEY = 'django-insecure-2j$i#b@!t1m_yc_!2^$g4or&9(hqq9+@e(_y#ereaoz5$q*yty'
DEV_SECRET_KEY = '2j$i#b@!t1m_yc_!2^$g4or&9(hqyc_!2^$g4or&9(hqq9+@e(_y#erq9+@e(_y#ereaoz5$q*yty'
SECRET_KEY = os.getenv('SECRET_KEY', DEV_SECRET_KEY)

ALLOWED_HOSTS = []

if not DEBUG:  ## when running in AWS
    ALLOWED_HOSTS.append('127.0.0.1')
    ALLOWED_HOSTS.append('mysite-dev222.us-east-1.elasticbeanstalk.com')
    ALLOWED_HOSTS.append('mysite-dev.1800infotech.com')
    try:
        EC2_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4').text
        ALLOWED_HOSTS.append(EC2_IP)
    except requests.exceptions.RequestException:
        pass


# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'health_check',                             # required
    'health_check.db',                          # stock Django health checkers
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.migrations',
    'ebhealthcheck.apps.EBHealthCheckConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'  # 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

if (not DEBUG):
    STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


## manage.py check --deploy fixes
SECURE_REDIRECT_EXEMPT = ['health/']
if (not DEBUG):
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
