from django.apps import AppConfig


class ChatConfig(AppConfig):
    name = 'chat'
    def ready(self):
        from .auto import update

        update.start()
