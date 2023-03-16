"""
Django settings for TaskManager project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-%9o0e*$ml)!&ubg!7u*mzmgjqrf$04x7xs8x@k@ymoyploo3&1'
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-%9o0e*$ml)!&ubg!7u*mzmgjqrf$04x7xs8x@k@ymoyploo3&1",
)

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool(os.environ.get("DJANGO_DEBUG", True))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "app_task",
    "api_task",
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

ROOT_URLCONF = 'TaskManager.urls'

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

WSGI_APPLICATION = 'TaskManager.wsgi.application'


# Database SQLite
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Подключаем MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'database': 'task_db',
#             'read_default_file': 'my.cnf',
#         },
#     }
# }

# Подключаем Postgres
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "task_db",
        "USER": "postgres",
        "PASSWORD": "pgadmin",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================================
# My Settings

# расшифровка операций
MY_OPER = {
    "list": "Список",
    "detail": "Просмотр",
    "add": "Добавление",
    "edit": "Редактирование",
    "delete": "Удаление",
}

# шаблон для создания тестовых пользователей
MY_TEST_USER = "test_user"
MY_TEST_PASS = "password"

# Логгирование
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        # "full": {
        #     "()": "django.utils.log.CallbackFilter",
        #     "callback": lambda rec: True,
        # },
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)-8s %(asctime)s"
            " [%(filename)s:%(lineno)4d] (%(name)s) %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "brief": {
            "format": "%(levelname)-8s %(asctime)s %(name)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "console_debug": {
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
            "level": "INFO",
            "formatter": "verbose",
        },
        "console_no_debug": {
            "class": "logging.StreamHandler",
            "filters": ["require_debug_false"],
            "level": "WARNING",
            "formatter": "brief",
        },
    },
    "loggers": {
        "": {  # root logger
            "level": "DEBUG",
            "handlers": ["console_debug", "console_no_debug"],
        },
        "more": {
            "level": "DEBUG" if DEBUG else "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        # "app_task": {
        #     "level": "DEBUG",
        #     "handlers": ["console"],
        #     "propagate": False,
        # },
        "app_task.services.perms": {
            "level": "INFO",
            "handlers": ["console_debug"],
            "propagate": False,
        },
        "django": {
        #     "level": os.environ.get("DJANGO_LOG_LEVEL", "INFO"),
            "level": "INFO",
            "handlers": ["console_debug"],
            "propagate": False,
        },
    },
}

# Настройки email
MY_EMAIL_ON = True
if MY_EMAIL_ON:
    if DEBUG:
        # стандартный вывод
        EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    else:
        EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
else:
    # фиктивный бэк - ничего не делает с сообщенияями
    EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
EMAIL_HOST = "127.0.0.1"
EMAIL_PORT = "465"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
ADMINS = (("Admin", "admin@none.none"),)
MANAGERS = ADMINS

# Login настройки
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Настройка пагинации
PAGINATE_BY = 5  # элементов на странице
# Если на последней странице элементов <= orphans, то добавляем их к предыдущей
PAGINATE_ORPHANS = 2

# REST настройки
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

# теги для видов сообщений
MESSAGE_TAGS = {
    10: "alert-dark",  # DEBUG - встроеный
    20: "alert-info",  # INFO - встроеный
    25: "alert-success",  # SUCCESS - встроеный
    30: "alert-warning",  # WARNING - встроеный
    40: "alert-danger",  # ERROR - встроеный
}
