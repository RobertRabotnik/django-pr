"""
Django settings for newspr project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os,sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Это для того, чтобы django искал наши приложеия в папке apps
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0,(os.path.join(PROJECT_ROOT,'apps')))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g4)br&&d0_aglqtg$*==p&ic5f6bb13qrulz3st-alzeon$rae'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]


# Посредники между запросом и ответом
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Путь к корневому url-конфигу 
ROOT_URLCONF = 'newspr.urls'

#Настройка шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT,'templates') # Допольнительные места, где django будет искать шаблоны, в данном случае в PROJECT_ROOT, папке templates
        ],
        'APP_DIRS': True, # Поиск шаблонов в приложении
        'OPTIONS': {
            # Переменные, которые можно использовать в шаблоне по умолчанию
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'newspr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# Настройка базы данных, у меня postgres, по умолчанию sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newspr-db2',
        'USER': 'postgres',
        'PASSWORD': '325baran+',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

#  Валидаторы для паролей (валидаторы - пидоры, проверяющие что-то на валидность, соответсвие каким-то правилам, требованиям, что-то типо того)

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

# язык
LANGUAGE_CODE = 'ru'

# Использование кастомной модели пользователя, которую я сам создал
AUTH_USER_MODEL = 'users.CustomUser'

# Часовой пояс
TIME_ZONE = 'Europe/Moscow'

# Это тоже связано с настройкой часового пояса
USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT,'static')

# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
