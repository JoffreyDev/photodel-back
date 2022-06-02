from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import AnonymousUser
from services.chat_service import get_chat_messages, messages_to_json, \
    create_new_messages, is_user_in_chat, update_profile_channel_name, \
    delete_profile_channel_name, filter_chat, chats_to_json, deleting_chat, \
    update_messages_status, get_receiver_profile

from services.request_chat_service import filter_request_chat, request_chats_to_json, \
    create_new_request_message, update_request_messages_status, get_request_chat_messages, \
    request_messages_to_json, is_user_in_request_chat, change_request_status, get_request_receiver_profile

import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def fetch_messages(self, data):
        """
        Команда для возврата всех сообшений чата
        Передается chat_id
        """
        messages = await get_chat_messages(self.room_name)
        receiver_profile = await get_receiver_profile(self.scope['user'], self.room_name)
        content = {
            "messages": await messages_to_json(messages, self.scope['user'], self.room_name),
            "name": receiver_profile.name,
            "surname": receiver_profile.surname,
            "avatar": receiver_profile.avatar.url,
            "receiver_id": receiver_profile.id,
            "online": receiver_profile.user_channel_name,
        }
        await self.send_message(content)

    async def new_messages(self, data):
        """
        Команда для создания нового сообщения
        и возврат его в json
        """
        message = await create_new_messages(data, self.room_name)
        if not message:
            return await self.send_chat_message({
                'command': 'new_message',
                'message': {
                    'error': 'Сообщение не было отправлено',
                }})
        if message:
            content = {
                'command': 'new_message',
                'message': {
                        'author_id': message.author.id,
                        'content': message.content,
                        'timestamp': str(message.timestamp),
                        'chat_id': message.chat.id,
                        'message_id': message.id,
                        "name": message.author.name,
                        "surname": message.author.surname,
                        "avatar": message.author.avatar.url,
                        "online": message.author.user_channel_name,
                    }
            }
            return await self.send_chat_message(content)

    async def update_message_status(self, data):
        """
        Обновление статусов сообщений в чате по списку id
        """
        response = await update_messages_status(data, self.room_name)
        return await self.send_message(response)

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_messages,
        'update_chat_status': update_message_status,
    }

    async def send_message(self, message):
        await self.send(text_data=json.dumps(message, cls=DjangoJSONEncoder))

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))

    async def send_chat_message(self, message):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.accept()
        if isinstance(self.scope['user'], AnonymousUser) or \
                not await is_user_in_chat(self.scope['user'], self.room_name):
            return await self.close(code=4123)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        if 'command' in data:
            await self.commands[data['command']](self, data)


class SiteConsumer(AsyncWebsocketConsumer):

    # TODO update
    async def history_request_chat(self, data):
        """
        Список истории чатов пользоватля
        """
        filter_queryset_chats = await filter_request_chat(self.scope['user'])
        content = {
            'request_chat_info': await request_chats_to_json(filter_queryset_chats, self.scope['user'])
        }
        await self.send_message(content)

    async def history_chat(self, data):
        """
        Список истории чатов пользоватля
        """
        filter_queryset_chats = await filter_chat(self.scope['user'])
        content = {
            'chat_info': await chats_to_json(filter_queryset_chats, self.scope['user'])
        }
        await self.send_message(content)

    async def delete_chat(self, data):
        """
        Удаление чата по id и возвращение истории чатов пользователя
        """
        await deleting_chat(data)
        await self.history_chat(data)

    commands = {
        'history_request_chat': history_request_chat,
        'history_chat': history_chat,
        'delete_chat': delete_chat,
    }

    async def send_message(self, message):
        await self.send(text_data=json.dumps(message, cls=DjangoJSONEncoder))

    async def connect(self):
        """
        Первоначальное соединение с вебсокетом,
        закрытие соединения если пользователь не авторизован
        добавление user_channel_name если пользователь успещно подключился к сокету
        """
        user = self.scope['user']
        if not isinstance(user, AnonymousUser):
            await update_profile_channel_name(user, self.channel_name)
            return await self.accept()
        return await self.close(code=4123)

    async def disconnect(self, close_code):
        """
        Закрытие вебоскета с пользователем и удаление имени канала из его профиля
        """
        if isinstance(self.scope['user'], AnonymousUser):
            return await self.close(code=4123)
        return await delete_profile_channel_name(self.scope['user'])

    async def receive(self, text_data):
        """
        Метод получения данных по вебсокету
        """
        data = json.loads(text_data)
        if 'command' in data:
            await self.commands[data['command']](self, data)


class RequestChatConsumer(AsyncWebsocketConsumer):
    """
    Класс для чата запросов
    """

    async def fetch_messages(self, data):
        """
        Команда для возврата всех сообшений чата
        Передается chat_id
        """
        messages = await get_request_chat_messages(self.room_name)
        receiver_profile = await get_request_receiver_profile(self.scope['user'], self.room_name)
        content = {
            "messages": await request_messages_to_json(messages, self.scope['user'], self.room_name),
            "name": receiver_profile.name,
            "surname": receiver_profile.surname,
            "avatar": receiver_profile.avatar.url,
            "receiver_id": receiver_profile.id,
            "online": receiver_profile.user_channel_name,
        }
        await self.send_message(content)

    async def new_request_message(self, data):
        """
        Команда для создания нового сообщения
        и возврат его в json
        """
        message = await create_new_request_message(data, self.room_name)
        if not message:
            return await self.send_chat_message({
                'command': 'new_message',
                'message': {
                    'error': 'Сообщение не было отправлено',
                }})
        if message:
            content = {
                'command': 'new_message',
                'message': {
                        'author_id': message.author.id,
                        'content': message.content,
                        'timestamp': str(message.timestamp),
                        'chat_id': message.chat.id,
                        'message_id': message.id,
                        "name": message.author.name,
                        "surname": message.author.surname,
                        "avatar": message.author.avatar.url,
                    }
            }
            return await self.send_chat_message(content)

    async def update_request_message_status(self, data):
        """
        Обновление статусов сообщений в чате по списку id
        """
        response = await update_request_messages_status(data, self.room_name)
        return await self.send_message(response)

    async def update_request_status(self, data):
        """
        Обновление статуса запроса
        """
        response = await change_request_status(self.scope['user'], data)
        if response.get('message', ''):
            return await self.fetch_messages(response)
        return await self.send_message(json.dumps(response))

    commands = {
        'fetch_messages': fetch_messages,
        'new_request_message': new_request_message,
        'update_request_message_status': update_request_message_status,
        'update_request_status': update_request_status,
    }

    async def send_message(self, message):
        await self.send(text_data=json.dumps(message, cls=DjangoJSONEncoder))

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))

    async def send_chat_message(self, message):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.accept()
        if isinstance(self.scope['user'], AnonymousUser) or \
                not await is_user_in_request_chat(self.scope['user'], self.room_name):
            return await self.close(code=4123)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        if 'command' in data:
            await self.commands[data['command']](self, data)