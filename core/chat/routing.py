from django.urls import path, include
from chat.consumers import ChatConsumer


"""
    This is another routing way beside the native django routing which is urls.py.
    This routing method is for the WebSockets for ASGI support of Django.
"""
websocket_urlpatterns = [
    path('', ChatConsumer.as_asgi()),
]