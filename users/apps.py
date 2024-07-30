from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # This function is to register our signals.py but we can also import the signals in the Models file
    def ready(self):
        import users.signals
