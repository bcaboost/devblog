# This is settings.py file
# this file is important 
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hb-t7yku*bh8ou1!4ob7i3i8gp=se($iwxz4qhgb%&9uq6^)+d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['http://devblognepal.herokuapp.com', 'devblognepal.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # third party apps
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'rest_framework.authtoken',
    'crispy_forms',
    # created apps
    'blogs',
    'pages'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_rest_framework.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_processors.main_all',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_rest_framework.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = BASE_DIR / 'static_CDN'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'homepage'
LOGOUT_REDIRECT_URL = 'homepage'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CKEDITOR_JQUERY_URL = STATIC_URL + 'plugins/jquery-3.3.1.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar' : [
            { 'name': 'basicstyles', 'items': [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting', 'RemoveFormat' ] },
            { 'name': 'clipboard', 'items': [ 'Undo', 'Redo', '-', 'Cut', 'Copy', 'Paste'] },
            { 'name': 'paragraph', 'items': [ 'NumberedList', 'BulletedList', '-', 'Blockquote', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock' ] },
            '/',
            { 'name': 'styles', 'items': ['Format','FontSize' ] },
            { 'name': 'colors', 'items': [ 'TextColor', 'BGColor' ] },
            { 'name': 'links', 'items': [ 'Link', 'Unlink' ] },
            { 'name': 'insert', 'items': [ 'Image', 'Table', 'HorizontalRule', '-', 'Smiley', 'SpecialChar' ] },
            { 'name': 'plugins', 'items': [ 'CodeSnippet' ] },
            { 'name': 'document', 'items': [ 'Source', '-', 'Preview' ] }
        ],
        'skin': 'moono',
        'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
    },
    'comment_editor' : {
        'toolbar' : [
            { 'name': 'basicstyles', 'items': [ 'Bold', 'Italic', 'Underline' ] },
            { 'name': 'clipboard', 'items': [ 'Undo', 'Redo', '-', 'Cut', 'Copy', 'Paste' ] },
            { 'name': 'paragraph', 'items': [ 'BulletedList' ] },
            { 'name': 'links', 'items': [ 'Link' ] },
            { 'name': 'insert', 'items': [ 'Smiley' ] },
            { 'name': 'plugins', 'items': [ 'CodeSnippet' ] },
            { 'name': 'document', 'items': [ 'Source'] }
        ],
        'width' : '100%',
        'skin' : 'moono-lisa',
        'extraPlugins' : ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
    }
}
CKEDITOR_UPLOAD_PATH = 'uploads'
CKEDITOR_IMAGE_BACKEND = "pillow"

# Activate Django-Heroku.
django_heroku.settings(locals())
