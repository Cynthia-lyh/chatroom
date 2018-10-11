# consumers.py

# -*- coding: utf-8 -*-

from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import async_to_sync
from django.utils import timezone
import json


# 自定义websocket处理类
class MyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # 创建连接时调用
        await self.accept()

        # 将新的连接加入到群组
        await self.channel_layer.group_add("chat", self.channel_name)


    async def receive(self, text_data=None, bytes_data=None):
        # 收到信息时调用
        print (text_data)
        # 信息单发
        # await self.send(text_data="Hello world!")

        # 信息群发
        time_now = timezone.now().strftime("%F %R ")
        await self.channel_layer.group_send(
            "chat",
            {
                "type": "chat.message",
                "username": time_now + json.loads(text_data)["username"] + "说:",
                "text": json.loads(text_data)["context"],
            },
            
        )

    async def disconnect(self, close_code):
        # 连接关闭时调用
        # 将关闭的连接从群组中移除
        await self.channel_layer.group_discard("chat", self.channel_name)

        await self.close()

    async def chat_message(self, event):
        # Handles the "chat.message" event when it's sent to us.
        await self.send(text_data=event["username"])
        await self.send(text_data=event["text"])