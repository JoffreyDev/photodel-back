from channels.db import database_sync_to_async
from chat.models import Chat, Message, Notification
from accounts.models import Profile
from django.db.models import Q, When, Case
from asgiref.sync import sync_to_async

from datetime import timedelta
import json
import channels.layers
import asyncio


def is_chat_unique(sender_id, receiver_id):
    """
    Проверка чата, при создании, на уникальность
    Проверка отправителя получателя и вещи
    """
    if sender_id == receiver_id:
        return False
    chat1 = Chat.objects.filter(Q(sender_id=sender_id) & Q(receiver_id=receiver_id)).first()
    chat2 = Chat.objects.filter(Q(sender_id=receiver_id) & Q(receiver_id=sender_id)).first()
    if chat1:
        return chat1.id
    elif chat2:
        return chat2.id
    return False


def get_interviewer_data(user, chat_id):
    """
    Получение параметров собеседника в чате
    """
    try:
        chat = Chat.objects.get(id=chat_id)
        if chat.sender_id.user == user:
            return chat.receiver_id.name, chat.receiver_id.surname, chat.receiver_id.user_channel_name, \
                   chat.receiver_id.avatar.url
        return chat.sender_id.name, chat.sender_id.surname, chat.sender_id.user_channel_name, \
               chat.sender_id.avatar.url
    except Chat.DoesNotExist:
        return None, None


def create_send_notification(receiver, type_note, text_note, model_id, sender_id):
    """
    Отправка уведолмения получателю если он онлайн
    """
    Notification.objects.create(type_note=type_note, text_note=text_note, model_id=model_id,
                                receiver=receiver, sender_id=sender_id)
    data = {}
    channel_name = None if not receiver else receiver.user_channel_name
    if channel_name:
        layer = channels.layers.get_channel_layer()
        asyncio.run(layer.send(channel_name, data))


@database_sync_to_async
def is_user_in_chat(user, room_name):
    """
    Проверка на нахождения пользователя в чате
    """
    try:
        profile = Profile.objects.get(user=user)
        chat = Chat.objects.filter((Q(sender_id=profile) | Q(receiver_id=profile)) & Q(id=int(room_name)))
        if chat:
            return True
        return False
    except ValueError:
        return False


@database_sync_to_async
def get_receiver_profile(user, chat_id):
    try:
        chat = Chat.objects.get(id=chat_id)
        return chat.sender_id
    except Chat.DoesNotExist:
        return None


@database_sync_to_async
def get_chat_messages(chat_id):
    """
    Получение сообщений в чате и возврат queryset
    """
    return Message.objects.filter(chat=chat_id).order_by('timestamp')


@database_sync_to_async
def create_new_messages(data, chat_id):
    """
    Создание нового сообщения
    """
    if data.get('message') and data.get('author_id'):
        author_user = Profile.objects.filter(id=data['author_id']).first()
        chat_instance = Chat.objects.filter(id=chat_id).first()
        if author_user and chat_instance:
            return Message.objects.create(author=author_user, content=data['message'], chat=chat_instance)
        return []
    return []


@sync_to_async
def messages_to_json(messages, user, chat_id):
    """
    Перебор queryset с сообщениями
    и возврат словаря для преобразование егоо в json
    """
    result = []
    for message in messages:
        current_time = message.timestamp + timedelta(hours=3)
        result.append(
            {
                'id': message.id,
                'content': message.content,
                'timestamp': str(current_time),
                'name': str(message.author.name),
                'surname': str(message.author.surname),
                'online': str(message.author.user_channel_name),
                'avatar': str(message.author.avatar.url),
            }
        )
    return result


@database_sync_to_async
def unread_message_ids(messages):
    """
    Вывод id всех непрочитанных сообщений
    """
    profile = Profile.objects.filter(user=self.scope['user']).first()
    return [message.id for message in messages.filter(status_read=False).exclude(author_id=profile.id)]


@database_sync_to_async
def last_message_status(messages, user_id):
    """
    Проверка статуса последнего сообщения пользователя
    """
    if not messages:
        return None
    if messages.last().author_id != user_id:
        return [messages.last().status_read, messages.last().id]


@database_sync_to_async
def update_messages_status(data, chat_id):
    """
    Обновление статуса прочитанных сообщений.
    Если прочитано status_read = True
    В качестве параметра приходить список id сообщений
    """
    if data.get('message_ids'):
        messages = Message.objects.filter(chat=chat_id, id__in=data['message_ids'])
        for message in messages:
            message.status_read = True
        Message.objects.bulk_update(messages, ['status_read'])
        return json.dumps({'success': 'updated'})
    return json.dumps({'error': 'not given parameters'})


@database_sync_to_async
def delete_profile_channel_name(user_id):
    """
    Обновление имени канала у пользователя если он не в онлайне
    """
    return Profile.objects.filter(user=user_id).update(user_channel_name=None)


@database_sync_to_async
def update_profile_channel_name(user_id, channel_name):
    """
    Обновление имени канала у пользователя если он в онлайне
    """
    return Profile.objects.filter(user=user_id).update(user_channel_name=channel_name)


@database_sync_to_async
def filter_chat(user):
    """
    Сортировка чатов по последнему сообщению
    В каком чате последнее сообщение тот и первый
    И фильтрация по пользователям чата,
    если юзера нет в чате он его не получит себе в список
    """
    messages = Message.objects.order_by('-id')
    list_chat_id = []
    for message in messages:
        chat_id = message.chat.id
        if chat_id not in list_chat_id:
            list_chat_id.append(chat_id)
    if not list_chat_id:
        order_list = Chat.objects.filter(Q(sender_id__user=user) | Q(receiver_id__user=user)) \
            .select_related('sender_id', 'receiver_id')
    else:
        chat = Chat.objects.filter(Q(sender_id__user=user) | Q(receiver_id__user=user))
        order_list = chat.filter(Q(id__in=list_chat_id))\
                                 .order_by(Case(*[When(id=n, then=i) for i, n in enumerate(list_chat_id)]))\
                                 .select_related('sender_id', 'receiver_id')
    return order_list


@database_sync_to_async
def deleting_chat(data, user):
    """
    Удаление чата по id чата и пользователь является учатсником чата
    """
    profile = Profile.objects.filter(user=user).first()
    if 'chat_id' in data:
        chat = Chat.objects.filter(id=data['chat_id']).first()
        if chat and (chat.sender_id == profile or chat.sender_id == profile):
            chat.delete()
            return True
        return False
    return False


@sync_to_async
def chats_to_json(chats, user):
    """
    Перебор queryset с чатами
    и возврат словаря для преобразование егоо в json
    """
    result = []
    profile = Profile.objects.filter(user=user).first()
    for chat in chats:
        chat_link_obj = chat.message_set.all()
        name, surname, online, avatar = get_interviewer_data(user, chat.id)
        result.append(
            {
                'id': chat.id,
                'sender_id': chat.sender_id.id,
                'receiver_id': chat.receiver_id.id,
                'last_message': chat_link_obj.last().content
                if chat_link_obj else None,
                'is_last_message': chat_link_obj.last().status_read
                if chat_link_obj and chat_link_obj.last().author == profile else None,
                'date_last_message': chat_link_obj.last().timestamp + timedelta(hours=3)
                if chat_link_obj else None,
                'name_interviewer': name,
                'surname_interviewer': surname,
                'avatar_last_message': chat_link_obj.last().author.avatar.url
                if chat_link_obj else None,
                'avatar_interviewer': avatar,
                'online': online,
                'not_read_messages': chat_link_obj.filter(status_read=False).exclude(author=profile).count()
                if chat_link_obj else None,
            }
        )
    return result
