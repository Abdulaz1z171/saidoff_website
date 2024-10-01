
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config('DEBUG', default=True, cast=bool)

SECRET_KEY = config('SECRET_KEY')
# DATABASE_URL = config('DATABASE_URL')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])


PORT = config('PORT', default=8000, cast=int)

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'saidoff.apps.SaidoffConfig',
    'rest_framework',
    'drf_yasg',
    
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default=5432, cast=int),
    }
}

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

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    # Add other languages as needed
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = config('STATIC_URL', '/static/')
MEDIA_URL = config('MEDIA_URL', '/media/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    # Title of the window
    "site_title": "Saidoff",

    # Title on the brand, and the login screen (19 chars max)
    "site_header": "Saidoff",

    # Title on the brand, and the login screen (19 chars max)
    "site_brand": "Saidoff Group",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "images/my-logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to My Admin Panel",

    # Copyright on the footer
    "copyright": "My Company Ltd",

    # The model admin to search from the search bar, i.e. a list of models
    "search_model": "auth.User",

    # Field name on user model to display as the user name in the admin
    "user_avatar": None,

    ############# Top Menu ##############
    # Links to put in the top bar
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://www.example.com/support", "new_window": True},
        {"app": "auth"},
    ],

    ############# Side Menu ##############
    # Whether to display the side menu (True or False)
    "show_sidebar": True,

    # Icons to use for each app in the side menu
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    # Custom icons for actions
    "icons_actions": {
        "delete": "fas fa-trash-alt",
        "edit": "fas fa-edit",
    },

    ############# UI Tweaks ##############
    # Options for the sidebar (expanded or collapsed)
    "sidebar": "expanded",

    # Theme options: "light", "dark", "auto"
    "theme": "dark",

    # Language bar (True or False)
    "show_language_switch": True,

    # Set to True for having a fullscreen button
    "show_fullscreen_button": True,

    # Set to True for having a dark-mode button
    "show_dark_mode_button": True,
}