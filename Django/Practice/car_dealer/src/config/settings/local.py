from .base import *  #noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_DB', 'car_dealer_local'),
        'USER': env.str('POSTGRES_USER', 'car_dealer'),
        'PASSWORD': env.str('POSTGRES_PASSWORD', 'car_dealer'),
        'HOST': env.str('DB_HOST', 'postgres'),
        'PORT': env.int('DB_PORT', 5432),
    }
}
