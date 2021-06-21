import os
from environs import Env

env = Env()
env.read_env()

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.getenv('DATABASES_HOST'),
        "PORT": os.getenv('DATABASES_PORT'),
        "NAME": os.getenv('DATABASES_NAME'),
        "USER": os.getenv('DATABASES_USER'),
        "PASSWORD": os.getenv('DATABASES_PASSWORD'),
    }
}

INSTALLED_APPS = ["datacenter"]

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ["*"]

DEBUG = env.bool("DEBUG")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    },
]


USE_L10N = True

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_TZ = True
