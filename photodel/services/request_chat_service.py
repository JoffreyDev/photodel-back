from channels.db import database_sync_to_async
from chat.models import RequestChat, RequestMessage
from film_places.models import FilmPlaces, FilmRequest
from accounts.models import Profile
from django.db.models import Q, When, Case
from asgiref.sync import sync_to_async
from datetime import timedelta
import json


def create_request_chat_and_message(sender_request, receiver_profile, request_id):
    """
    Создание чата и сооющения при создание запроса на съемку
    """
    chat = RequestChat.objects.create(
        request_sender_id=sender_request, request_receiver_id=receiver_profile)
    RequestMessage.objects.create(
        request_id=request_id, chat_id=chat.id, author_id=sender_request)
    return True


def get_interviewer_data(user, chat_id):
    """
    Получение параметров собеседника в чате
    """
    try:
        chat = RequestChat.objects.get(id=chat_id)
        if chat.request_sender.user == user:
            return chat.request_receiver.name, chat.request_receiver.surname, \
                chat.request_receiver.user_channel_name, chat.request_receiver.avatar.url
        return chat.request_sender.name, chat.request_sender.surname, \
            chat.request_sender.user_channel_name, chat.request_sender.avatar.url
    except RequestChat.DoesNotExist:
        return None, None, None


@database_sync_to_async
def get_request_receiver_profile(user, chat_id):
    try:
        chat = RequestChat.objects.get(id=chat_id)
        if chat.request_sender.user.id == user.id:
            return chat.request_receiver
        return chat.request_sender
    except RequestChat.DoesNotExist:
        return None


@database_sync_to_async
def is_user_in_request_chat(user, room_name):
    """
    Проверка на нахождения пользователя в чате
    """
    try:
        profile = Profile.objects.get(user=user)
        chat = RequestChat.objects.filter((Q(request_sender=profile) | Q(
            request_receiver=profile)) & Q(id=int(room_name)))
        if chat:
            return True
        return False
    except ValueError:
        return False


@database_sync_to_async
def get_request_chat_messages(chat_id):
    """
    Получение сообщений в чате и возврат queryset
    """
    return RequestMessage.objects.filter(chat=chat_id).order_by('timestamp')


@database_sync_to_async
def create_new_request_message(data, chat_id):
    """
    Создание нового сообщения
    """
    if data.get('message') and data.get('author_id'):
        author_user = Profile.objects.filter(id=data['author_id']).first()
        chat_instance = RequestChat.objects.filter(id=chat_id).first()
        if author_user and chat_instance:
            return RequestMessage.objects.create(author=author_user, content=data['message'], chat=chat_instance)
        return []
    return []


@database_sync_to_async
def update_request_messages_status(data, chat_id):
    """
    Обновление статуса прочитанных сообщений.
    Если прочитано status_read = True
    В качестве параметра приходить список id сообщений
    """
    if data.get('message_ids'):
        messages = RequestMessage.objects.filter(
            chat=chat_id, id__in=data['message_ids'])
        for message in messages:
            message.status_read = True
        RequestMessage.objects.bulk_update(messages, ['status_read'])
        return json.dumps({'success': 'updated'})
    return json.dumps({'error': 'not given parameters'})


@database_sync_to_async
def filter_request_chat(user):
    """
    Сортировка чатов по последнему сообщению
    В каком чате последнее сообщение тот и первый
    И фильтрация по пользователям чата,
    если юзера нет в чате он его не получит себе в список
    """
    messages = RequestMessage.objects.order_by('-id')
    list_chat_id = []
    for message in messages:
        chat_id = message.chat.id
        if chat_id not in list_chat_id:
            list_chat_id.append(chat_id)
    if not list_chat_id:
        order_list = RequestChat.objects.filter(Q(request_sender__user=user) | Q(request_receiver__user=user)) \
            .select_related('request_sender', 'request_receiver')
    else:
        chat = RequestChat.objects.filter(
            Q(request_sender__user=user) | Q(request_receiver__user=user))
        order_list = chat.filter(Q(id__in=list_chat_id))\
            .order_by(Case(*[When(id=n, then=i) for i, n in enumerate(list_chat_id)]))\
            .select_related('request_sender', 'request_receiver')
    return order_list


@database_sync_to_async
def change_request_status(user, data):
    """
    Изменение статуса запроса
    """
    if not data.get('filming_status') or not data.get('request_id'):
        return {'error': 'not given parameters'}
    try:
        request = FilmRequest.objects.get(id=data.get('request_id'))
        status = data.get('filming_status')

        if request.filming_status == 'NEW' and request.receiver_profile.user != user \
                and (status == 'ACCEPTED' or status == 'REJECTED'):
            request.filming_status = status
            request.save()
            return {'message': 'You successful update filming status'}
        if request.filming_status == 'ACCEPTED' and request.profile.user != user \
                and (status == 'COMPLETED' or status == 'UNCOMPLETED'):
            request.filming_status = status
            request.save()
            return {'message': 'You successful update filming status'}
        return {'error': f'You not permissions to change status'}
    except FilmRequest.DoesNotExist:
        return {'error': 'not found request'}


@sync_to_async
def request_messages_to_json(messages, user, chat_id):
    """
    Перебор queryset с сообщениями
    и возврат словаря для преобразование егоо в json
    """
    result = []
    for message in messages:
        current_time = message.timestamp + timedelta(hours=3)
        name, surname, online, avatar = get_interviewer_data(user, chat_id)
        if message.request:
            request = message.request
            result.append(
                {
                    'id': message.id,
                    'content': message.content,
                    'timestamp': str(current_time),
                    'name': str(message.author.name),
                    'surname': str(message.author.surname),
                    'avatar': str(message.author.avatar.url),
                    'online': str(message.author.user_channel_name),
                    'filming_timestamp': str(request.filming_timestamp),
                    'hours_duration': str(request.hours_duration),
                    'filming_type': str(request.filming_type),
                    'filming_status': str(request.filming_status),
                    'place_filming': str(request.place_filming),
                    'count_person': str(request.count_person),
                    'filming_budget': str(request.filming_budget),
                    'need_makeup_artist': str(request.need_makeup_artist),
                    'description': str(request.description),
                    'author_id': int(message.author.id)
                }
            )
        else:
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


@sync_to_async
def request_chats_to_json(chats, user):
    """
    Перебор queryset с чатами
    и возврат словаря для преобразование егоо в json
    """
    result = []
    profile = Profile.objects.filter(user=user).first()
    for chat in chats:
        chat_link_obj = chat.requestmessage_set.all()
        name_interviewer, surname, online, avatar = get_interviewer_data(
            user, chat.id)
        result.append(
            {
                'id': chat.id,
                'sender_id': chat.request_sender.id,
                'receiver_id': chat.request_receiver.id,
                'avatar': avatar,
                'avatar_last_message': chat_link_obj.last().author.avatar.url
                if chat_link_obj else None,
                'is_last_message': chat_link_obj.last().status_read
                if chat_link_obj and chat_link_obj.last().author_id == profile.id else None,
                'date_last_message': chat_link_obj.last().timestamp + timedelta(hours=3)
                if chat_link_obj else None,
                'name_interviewer': name_interviewer,
                'surname_interviewer': surname,
                'online': online,
                'not_read_messages': chat_link_obj.filter(status_read=False).exclude(author_id=profile.id).count()
                if chat_link_obj else None,

                'request_id': chat_link_obj.first().request.id
                if chat_link_obj.first() and chat_link_obj.first().request else None,
                'request_executor_id': chat_link_obj.first().request.receiver_profile.id
                if chat_link_obj.first() and chat_link_obj.first().request else None,
                'request_status': chat_link_obj.first().request.filming_status
                if chat_link_obj.first() and chat_link_obj.first().request else None,
                'filming_timestamp': chat_link_obj.first().request.filming_timestamp
                if chat_link_obj.first() and chat_link_obj.first().request else None,
                'place_filming': chat_link_obj.first().request.place_filming
                if chat_link_obj.first() and chat_link_obj.first().request else None,
                'hours_duration': chat_link_obj.first().request.hours_duration
                if chat_link_obj.first() and chat_link_obj.first().request else None,
            }
        )
    return result
