from django.apps import AppConfig


class AwwardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'awwards'

    """
    connect the signals file with the app.py file ready function in order to use them.
    """
    def ready(self):
        import awwards.signals