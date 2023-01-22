from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_assesment.apps.user'

    def ready(self):
        import test_assesment.apps.user.signals
