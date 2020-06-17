from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from . import models
from channels.auth import login
class ChatConsumerEditor(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_name = "hello"
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # print(message)

        await login(self.scope, user)

        await database_sync_to_async(self.scope["session"].save())

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
        }))
        await self.save_message(message)
    
    @database_sync_to_async
    def save_message(self, message):
        texte = message['mes']
        auteur = User.objects.get(username=str(message['user']))

        mess = models.Message(
            message=texte,
            author=auteur
        )
        mess.save()