"""
Django settings for follow_up_project project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import sys
import os
from pathlib import Path


import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-abl9ym&=_py-b-t^-5z8%+!#p%iresgkgtvbh#f82xv%jw7d#p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','164.92.239.39']

# CFSF_TRUSTED_ORIGINS = ['www.tcgcms.sitanetorbit.com', 'tcgcms.sitanetorbit.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'follow_app',
    'pastorate',
    # 'celery_results',
    'accounts',
    'coordinators',
    'team_members',
    'facilitator',
    'student',
    'career',
    'business',
    'kbn',
    'crispy_forms',
    'asset_system',
    'tinymce',

    'storages',
  
   
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'follow_up_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'follow_up_project.wsgi.application'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


AUTH_USER_MODEL = 'accounts.User'  # Replace 'accounts.User' with the correct app label and model name

# local host

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DATABASE_NAME'),  # The name of your database
#         'USER': os.getenv('DATABASE_USER'),  # The database user
#         'PASSWORD': os.getenv('DATABASE_PASSWORD'),  # The user password
#         'HOST': 'localhost',  # The service name from docker-compose.yml
#         'PORT': '5432',  # Default PostgreSQL port
#     }
# }

# AWS

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME', ''),
#         'USER': os.environ.get('DB_USER', ''),
#         'PASSWORD': os.environ.get('DB_PASSWORD', ''),
#         'HOST': os.environ.get('DB_HOST', ''),
#         # 'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'tcgc_cms_db',
#         'USER': 'tcgc_cms_user',
#         'PASSWORD': 'Completed1234',
#         'HOST': 'database-1.ctqg0cgman7j.af-south-1.rds.amazonaws.com',
#         # 'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tcgc_cms_db',
        'USER': 'tcgc_cms_user',
        'PASSWORD': 'Completed1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}






# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'tcgc_db',
#         'USER': 'postgres',
#         'PASSWORD': 'People',
#         'HOST': 'localhost',
      
#         'PORT': '5432',          
#     }
# }






# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

 
MEDIA_URL = 'media/'
MEDIA_ROOT = '/home/bayo/tcgc_cms/media/' 

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# settings.py
STATIC_URL = '/static/'  # URL to serve static files
STATIC_ROOT = '/home/bayo/tcgc_cms/static/'  # Directory where static files will be stored


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATIC_ROOT = '/home2/thecity2/public_html/followtheminchrist/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
# STATICFILES_DIRS = [
    
#     'follow_up_project/static',
#     # os.path.join(BASE_DIR, 'your_app/static'),
# ]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/home2/thecity2/public_html/followtheminchrist/media/'
# MEDIA_ROOT = BASE_DIR /'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# STATIC_URL = '/static/'




# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",  # For media files
#         "OPTIONS": {
#             "location": "media",  # Folder within your S3 bucket for media files
#         },
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",  # For static files
#         "OPTIONS": {
#             "location": "static",  # Folder within your S3 bucket for static files
#         },
#     },
# }


# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'





# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
# AWS_S3_REGION_NAME = 'af-south-1'  # Specify the correct region of your bucket

# AWS_S3_CUSTOM_DOMAIN = '%s.s3.af-south-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# AWS_S3_FILE_OVERWRITE = False



# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         "OPTIONS": {
#             "location": "media",
#         },
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         "OPTIONS": {
#             "location": "static",
#         },
#     },
# }
