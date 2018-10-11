# routing.py

from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from . import consumer


application = ProtocolTypeRouter({

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("chatroom/websocket", consumer.MyConsumer),
            path("chatroom/chatroom", consumer.MyConsumer),
        ])
    ),
})