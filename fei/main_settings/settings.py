"""
Django settings for main_settings project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from share.config_mysql import DATABASES_MYSQL
import os

# for sphinx , setup env variable DJANGO_SETTINGS_MODULE
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
# import django
# django.setup()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e)fn@*u@%+x7kxd^+&_vd5gnd%&3r#nopn-+)k3u$2fm$8l67a'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DJANGO_DEBUG'):
    DEBUG = True
else:
    DEBUG = False
# DEBUG = False

ALLOWED_HOSTS = ["*", ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_demo1',
    'app_models',
    'rest_framework',
    'rest_framework.authtoken',
    'app_drf',
    'app_img',
    'app_clientip',
    'app_comments',
    'app_cache',
    'app_sysinfo',
]

MIDDLEWARE = [
    # 自定义middleware，检查response headers
    'fei_middlewares.headers_info.response_headers',
    'fei_middlewares.drf_token_info.drf_user_info',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # 检查信息
    'fei_middlewares.headers_info.request_headers',
    # 过滤一下测试用户，不让它改密码
    'fei_middlewares.user_filter.disable_user_change_pass',
    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # custom middleware: current_user
    'fei_middlewares.logging_user.django_current_user',
    'fei_middlewares.logging_user.logging_user',
    'fei_middlewares.rate_limit.ratelimit',

    'fei_middlewares.data_initial.initial_user_extra',
    'fei_middlewares.data_initial.initial_user_asset',
    'fei_middlewares.generate_token.generate_token_if_not_exist',
]

ROOT_URLCONF = 'main_settings.urls'

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

                # 自定义context processors
                'fei_contextprocessors.page_header.context_fei',
            ],
        },
    },
]

WSGI_APPLICATION = 'main_settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = DATABASES_MYSQL

# 不使用AbstractUser来扩展用户模型
# AUTH_USER_MODEL = 'app_models.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # 禁止CommonPasswordValidator，则可以使用任何简单的password
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'PRC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'collect_to'
STATICFILES_DIRS = ['collect_serve', ]

# django 认证
AUTHENTICATION_BACKENDS = [
     'django.contrib.auth.backends.ModelBackend', 
     'fei_backends.fei_auth.FeiAuth',
    #  'fei_backend.my_auth_backend_1.MyBackend1',
    ]

# for app_drf
REST_FRAMEWORK = {
    # for drf pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,

    # for drf authentication
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    # 'UNICODE_JSON': True,
    # 'COMPACT_JSON': True,
    
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    #     ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    #     ]
}

from share.config_redis import REDIS_LOCATION
# 启用redis作为django的cache backend
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 10},
        }
    }
}

# dummy cache
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }
