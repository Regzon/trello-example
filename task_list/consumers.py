import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class TaskListConsumer(WebsocketConsumer):

    def connect(self):
        self.access_key = self.scope['url_route']['kwargs']['key']
        self.group_name = f'task_list_{self.access_key}'
        # Join group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )
        # Accept the connection
        self.accept()

    def disconnect(self, close_code):
        # Leave group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name,
        )

    # Receive message from Websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        task_name = text_data_json['name']
        # Send to group
        data = {
            'type': 'add_task',
            'name': task_name,
        }
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            data,
        )

    # Receive message from group
    def add_task(self, event):
        task_name = event['name']
        # Send to Websocket
        self.send(text_data=json.dumps({
            'name': task_name,
        }))
