from datetime import timedelta

from config.env_config import env_config

BASE_DIR = env_config.BASE_DIR

ALLOWED_HOSTS = env_config.ALLOWED_HOSTS

SECRET_KEY = env_config.DJANGO_SK

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "drf_spectacular",
    "users",
    "products",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env_config.DB.NAME,
        "USER": env_config.DB.USER,
        "PASSWORD": env_config.DB.PASSWORD,
        "HOST": env_config.DB.HOST,
        "PORT": env_config.DB.PORT,
    },
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# USER MODEL
AUTH_USER_MODEL = "users.CustomUser"

# SIMPLE_JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=env_config.AUTH.ACCESS_TOKEN_LIFETIME_MINUTES,
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        minutes=env_config.AUTH.REFRESH_TOKEN_LIFETIME_MINUTES,
    ),
    "ROTATE_REFRESH_TOKENS": env_config.AUTH.ROTATE_REFRESH_TOKEN,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "LEEWAY": 10,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
}

# CORS
CORS_ALLOW_ALL_ORIGINS = env_config.CORS.ALLOW_ALL_ORIGINS

CORS_ALLOW_CREDENTIALS = env_config.CORS.ALLOW_CREDENTIALS

if not env_config.CORS.ALLOW_ALL_ORIGINS:
    CORS_ALLOWED_ORIGINS = env_config.CORS.ALLOWED_ORIGINS

CORS_ALLOW_HEADERS = env_config.CORS.ALLOW_HEADERS

# Rest framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "base.exceptions.base_exception_handler",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 25,
}

# drf-spectacular
SPECTACULAR_SETTINGS = {
    "TITLE": "Favorite Products Test",
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVE_PERMISSIONS": ("rest_framework.permissions.IsAdminUser",),
    "SERVE_AUTHENTICATION": ("rest_framework.authentication.SessionAuthentication",),
}
