from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from . import models
from channels.auth import login
from datetime import datetime
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
        actu = await self.get_all_chat(self.room_name)
        await self.accept()
        # await self.get_all_chat(self.room_name)
        # self.mess_histo =  await database_sync_to_async(self.get_all_chat(self.room_name))
        # print(mess_histo)
        # for m in histo:
        #     data = {
        #         'author': m.user.username,
        #         'message': m.message,
        #         'date_add': m.date_add.strtftime('%d%m%Y'),
        #     }
        #     await self.send(text_data=json.dumps(data))

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
        try:
            messagein = message['mes']
            userin = message['user']
            
            print(messagein)
            print(userin)
        except Exception as e:
            print(str(e))
            pass

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )
        
        await self.save_message(message)

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
        }))    
    @database_sync_to_async
    def save_message(self, message):
        texte = message['mes']
        author = message['user']
        auteur = User.objects.filter(username=author)[:1].get()
        salon = models.salon.objects.filter(slug=message['slug'])[:1].get()

        mess = models.Message(
            message=texte,
            author=auteur,
            salon=salon
        )
        mess.save()
    
    @database_sync_to_async
    def get_all_chat(self, salon):
        salon = models.salon.objects.filter(slug=salon)[:1].get()
        print(salon)
        return models.Message.objects.filter(status=True, salon=salon).order_by('date_add')