from django.db import models
from accounts.models import Profile
from film_places.models import FilmRequest
from django.utils import timezone


class Chat(models.Model):
    sender_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    is_sender_hide_chat = models.BooleanField(default=False)
    is_receiver_hide_chat = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}'


class Message(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author_message')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    status_read = models.BooleanField(default=False)


class RequestChat(models.Model):
    request_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='request_sender')
    request_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='request_receiver')

    def __str__(self):
        return f'{self.pk}'


class RequestMessage(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='request_author_message')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    chat = models.ForeignKey(RequestChat, on_delete=models.CASCADE)
    status_read = models.BooleanField(default=False)
    request = models.ForeignKey(FilmRequest, on_delete=models.CASCADE, blank=True,
                                related_name='request_author_message', null=True)


class Notification(models.Model):

    TYPE_NOTE_CHOICE = [
        ('MESSAGE', 'новое сообшение'),
        ('REQUEST', 'Новое запрос'),
        ('REQUEST_MESSAGE', 'Новое сообщение в запросе'),
        ('UPDATE_REQUEST', 'Обновление статуса запроса'),
        ('LIKE_PROFILE', 'Лайк профиля'),
        ('LIKE_PHOTO', 'Лайк фото'),
        ('LIKE_PHOTO_SESSION', 'Лайк фотосессии'),
        ('LIKE_PLACE', 'Лайк места'),
        ('FAVORITE_PROFILE', 'Избранное профиля'),
        ('FAVORITE_PHOTO', 'Избранное фото'),
        ('FAVORITE_PHOTO_SESSION', 'Избранное фотосессии'),
        ('FAVORITE_PLACE', 'Избранное места'),
        ('COMMENT_PROFILE', 'Коммент профиля'),
        ('COMMENT_PHOTO', 'Коммент фото'),
        ('COMMENT_PHOTO_SESSION', 'Коммент фотосессии'),
        ('COMMENT_PLACE', 'Коммент места'),
    ]

    type_note = models.CharField(max_length=25, choices=TYPE_NOTE_CHOICE, null=True)
    text_note = models.TextField(null=True)
    is_read = models.BooleanField(default=False, null=True)
    timestamp = models.DateTimeField(default=timezone.localtime)
    model_id = models.IntegerField()

    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True,
                               related_name='notification_sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='notification_receiver')

