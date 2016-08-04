from settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'saikumar$rentspace',
        'USER':'saikumar',
        'PASSWORD':'rentspace',
        'PORT':3306,
        'HOST': 'saikumar.mysql.pythonanywhere-services.com',
    }
}
