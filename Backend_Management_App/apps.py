from django.apps import AppConfig


class BackendManagementAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Backend_Management_App'

    def ready(self):
        import Backend_Management_App.signals
