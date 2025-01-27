"""
Django settings for ictcg project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from glob import glob
from pathlib import Path

import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import ignore_logger

production = os.getenv("DJANGO_ENV") == "production"
local_access = "LOCAL_ACCESS" in os.environ or "ALLOWED_HOSTS" not in os.environ

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "%r6!#s1!$6y9s7-fz3_ua@x7_mkuq2jvg^ava^1zy@_sq(0z&%")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", str(not production)) == "True"

ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]", "0.0.0.0"]  # noqa: S104 # Docker
if "ALLOWED_HOSTS" in os.environ:
    ALLOWED_HOSTS.extend(os.getenv("ALLOWED_HOSTS").split(","))


# Application definition

# https://docs.wagtail.org/en/stable/advanced_topics/add_to_django_project.html#settings-py
INSTALLED_APPS = [
    "base",
    "guidelines",
    "streams",
    "sponsors",
    "navigation",
    "modules",
    "case_studies",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    # https://docs.wagtail.org/en/stable/reference/contrib/legacy_richtext.html
    "wagtail.contrib.legacy.richtext",
    "wagtail.core",
    # https://docs.wagtail.org/en/stable/reference/contrib/settings.html
    "wagtail.contrib.settings",
    # https://docs.wagtail.org/en/v5.2.7/reference/contrib/modeladmin/index.html
    "wagtail.contrib.modeladmin",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # https://docs.wagtail.org/en/stable/reference/contrib/sitemaps.html
    "django.contrib.sitemaps",
    "wagtailtrans",
]


MIDDLEWARE = [
    # This site is not affected by BREACH, because it doesn't reflect user data.
    # https://docs.djangoproject.com/en/4.2/ref/middleware/#django.middleware.gzip.GZipMiddleware
    "django.middleware.gzip.GZipMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Replaces django.middleware.locale.LocaleMiddleware.
    # https://wagtailtrans.readthedocs.io/en/latest/getting_started.html
    "wagtailtrans.middleware.TranslationMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # https://docs.wagtail.org/en/stable/reference/contrib/redirects.html
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "ictcg.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "ictcg" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "ictcg.context_processors.from_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "ictcg.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(default="postgresql:///digitalbuyingguide?application_name=digitalbuyingguide"),
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Project-specific Django configuration

LOCALE_PATHS = glob(str(BASE_DIR / "**" / "locale"))

STATIC_ROOT = BASE_DIR / "static"

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATICFILES_DIRS = [BASE_DIR / "ictcg" / "static"]  # gulpfile.babel.js

# https://docs.djangoproject.com/en/4.2/topics/logging/#django-security
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "null": {
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG" if production else os.getenv("LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}

# https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
if production and not local_access:
    # Run: env DJANGO_ENV=production SECURE_HSTS_SECONDS=1 ./manage.py check --deploy
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_REFERRER_POLICY = "same-origin"  # default in Django >= 3.1

    # https://docs.djangoproject.com/en/4.2/ref/middleware/#http-strict-transport-security
    if "SECURE_HSTS_SECONDS" in os.environ:
        SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS"))
        SECURE_HSTS_INCLUDE_SUBDOMAINS = True
        SECURE_HSTS_PRELOAD = True

# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-proxy-ssl-header
if "DJANGO_PROXY" in os.environ:
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

LANGUAGES = (
    ("en", "English"),
    ("es", "LA Spanish"),
    ("id", "Bahasa"),
)

MEDIA_ROOT = os.getenv("MEDIA_ROOT", "/data/media/" if production else BASE_DIR / "media/")
MEDIA_URL = "media/"

if production:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": os.getenv("REDIS_URL", "redis://localhost:6379/0"),
            "TIMEOUT": 604800,  # 7 days
        }
    }

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"

FIXTURE_DIRS = [BASE_DIR / "tests" / "fixtures"]


# Dependency configuration

if "SENTRY_DSN" in os.environ:
    # https://docs.sentry.io/platforms/python/logging/#ignoring-a-logger
    ignore_logger("django.security.DisallowedHost")
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
    )

# https://docs.wagtail.org/en/stable/reference/settings.html
WAGTAIL_SITE_NAME = "ictcg"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
#
# WAGTAILADMIN_BASE_URL in 3.0.
# https://docs.wagtail.org/en/stable/releases/3.0.html#other-features
BASE_URL = "https://digitalbuying.open-contracting.org"

# https://wagtailtrans.readthedocs.io/en/latest/settings.html
WAGTAILTRANS_HIDE_TRANSLATION_TREES = True


# Project configuration

FATHOM = {
    "domain": os.getenv("FATHOM_ANALYTICS_DOMAIN") or "cdn.usefathom.com",
    "id": os.getenv("FATHOM_ANALYTICS_ID"),
}
