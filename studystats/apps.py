from django.apps import AppConfig


class StudystatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studystats'

    def ready(self):
        import studystats.signals
