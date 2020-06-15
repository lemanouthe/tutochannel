from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<slug:room_name>/', consumers.ChatConsumerEditor),
    # path('ws/chat/salon/', consumers.ChatConsumerGroup),
    # path('ws/suggest/suggestion/', consumers.ChatSuggestion),
]