from django.apps import AppConfig


class SaidoffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'saidoff'

    
    def ready(self):

        import saidoff.translation
