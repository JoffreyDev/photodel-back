from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    path('ws/request_chat/<str:room_name>/',
         consumers.RequestChatConsumer.as_asgi()),
    path('ws/', consumers.SiteConsumer.as_asgi()),
]
