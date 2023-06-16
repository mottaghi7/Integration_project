import os
from pathlib import Path
import activity_log

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import taggit.apps
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)st&_clz^!5=*e&hu_ja5^vneq=$$i*c!8(&4a*4-1_3*0=k=@'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',

    # Installed App
    'UserManager.apps.UsermanagerConfig',

    # Third party app
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'django_jalali',
    'jalali_date',
    'ckeditor',
    'taggit',
    'activity_log',
    'azbankgateways',
    'captcha',
]

MIDDLEWARE = [
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'activity_log.middleware.ActivityLogMiddleware',
]

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

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

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# Media files (Image, Video, etc)
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# taggit settings
taggit.apps.TaggitAppConfig.verbose_name = 'تگ زن'

# custom user manager setting
LOGIN_REDIRECT_URL = 'UserManager:dashboard'
# LOGOUT_REDIRECT_URL = 'Home:index'
LOGIN_URL = reverse_lazy('UserManager:login')
AUTH_USER_MODEL = 'UserManager.User'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'UserManager.backends.CaseInSensitiveModelBackend'
]

# activity log settings
ACTIVITYLOG_ANONYMOUS = True
ACTIVITYLOG_LAST_ACTIVITY = False

ACTIVITYLOG_METHODS = ('POST', 'GET', 'PUT', 'PATCH')
ACTIVITYLOG_EXCLUDE_STATUSES = ()
# ACTIVITYLOG_EXCLUDE_URLS = ('/user/signin/', )
ACTIVITYLOG_LAST_ACTIVITY = True

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ssa.ceuk@gmail.com'
EMAIL_HOST_PASSWORD = 'ssaMaster1400'
SERVER_EMAIL = 'mh.mohammadzade98@gmail.com'
EMAIL_ADMIN_LIST = ['mh.mohammadzade98@gmail.com']

MAX_UPLOAD_SIZE = 5242880
FILE_CONTENT_TYPE = ['image', 'video', ]

# rest framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    # Django Rest Framework Authtoken Setting
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.TokenAuthentication'
    # ],

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter'
    ],

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# payment

AZ_IRANIAN_BANK_GATEWAYS = {
    'GATEWAYS': {
        'IDPAY': {
            'MERCHANT_CODE': '36fdb48c-3b59-4ebe-b550-a15040bcadb4',
            'METHOD': 'POST',
            'X_SANDBOX': 1,
        },
    },
    'IS_SAMPLE_FORM_ENABLE': True,
    'DEFAULT': 'IDPAY',
    'CURRENCY': 'IRT',
    'TRACKING_CODE_QUERY_PARAM': 'tc',
    'TRACKING_CODE_LENGTH': 16,
    'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader',
    'BANK_PRIORITIES': [
    ],
}

# google captcha settings
RECAPTCHA_PUBLIC_KEY = '6LdG9fsdAAAAALZ9A2L6rimOLEx9cZNS-Ohas7RF'
RECAPTCHA_PRIVATE_KEY = '6LdG9fsdAAAAAFNygu7_jX30c0IrbEcW8vEdz7sZ'
