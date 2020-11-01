from django.apps import AppConfig


class SocialAppConfig(AppConfig):
    name = 'donation_app'

    def ready(self):
        import donation_app.users.signals