from django.apps import AppConfig
from . import wrapper


class DjangoPynotificationsConfig(AppConfig):
    name = 'django_pynotifications'
    verbose_name = 'django Pynotification'

    def ready(self):
        wrapper.init()
