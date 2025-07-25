import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LoanApplicationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
   
        await self.channel_layer.group_add("loan_applications_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard("loan_applications_group", self.channel_name)

   
    async def receive(self, text_data):
        pass  
    async def loan_application_notification(self, event):
       
        await self.send(text_data=json.dumps(event["content"]))
