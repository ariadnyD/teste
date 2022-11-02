from django.apps import AppConfig


class PrivadoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'privado'

    def ready(self):
        import privado.signals