from django.contrib import admin
from .models import Chat, Message, RequestChat, RequestMessage


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['sender_id', 'receiver_id', 'id', ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'chat', 'status_read', 'id', ]


@admin.register(RequestChat)
class RequestChatAdmin(admin.ModelAdmin):
    list_display = ['request_sender', 'request_receiver', 'id', ]


@admin.register(RequestMessage)
class RequestMessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'chat', 'status_read', 'id', 'request']