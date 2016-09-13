from settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'saikumar$rahilodb',
        'USER':'saikumar',
        'PASSWORD':'rahilodb',
        'PORT':3306,
        'HOST': 'saikumar.mysql.pythonanywhere-services.com',
    }
}
