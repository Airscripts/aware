import os
import dj_database_url
from pathlib import Path

DEBUG = True
ROOT_URLCONF = "morazyne.urls"
DATABASES["default"].update(db_from_env)
WSGI_APPLICATION = "morazyne.wsgi.application"
BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1"]
SECRET_KEY = "1q*dv&q1@$g13ng-dfucs-%zzg$on!3uqww*(w9!h8!&-n4f(#"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

db_from_env = dj_database_url.config(conn_max_age=600)

USE_TZ = True
USE_I18N = True
USE_L10N = True
TIME_ZONE = "UTC"
LANGUAGE_CODE = "it"
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR,"media")
STATIC_ROOT = os.path.join(BASE_DIR,"static")
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
STATICFILES_DIRS = [os.path.join(BASE_DIR,"project_name/static")]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "warehouse.apps.WarehouseConfig",
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

TEMPLATES = [
    {
        "APP_DIRS": True,
        "DIRS": [BASE_DIR / "templates"],
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    "default": {
        "PORT": ",
        "USER": "admin",
        "NAME": "admin",
        "HOST": "localhost",
        "PASSWORD": "admin",
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]