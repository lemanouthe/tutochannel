#------ WS
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def hello():
    print("Hello world")
    
    layer = get_channel_layer()
    data = {
        'mes': 'Le cours prend fin dans 10 minutes',
        'user': "Admin",
    }
    async_to_sync(layer.group_send)('chat_salut', {
        'type': 'chat_message',
        'message': data
    })