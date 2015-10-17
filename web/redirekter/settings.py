# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SITE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&t@o*1tl*w5n@19qdg^=(4kufkzdx!c@bc-^#nniw&$54d-+#*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'widget_tweaks',
    'redirekter.apps.reviews',
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
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',
)

ROOT_URLCONF = 'redirekter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'redirekter.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'redirekter'),
        'USER': os.environ.get('DB_USER', 'redirekter'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'redirekter'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': int(os.environ.get('DB_PORT', '5432')),
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

STATICFILES_DIRS = (
    os.path.join(SITE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "static")

SOCIAL_AUTH_GITHUB_KEY = os.getenv('GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('GITHUB_SECRET')
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'
