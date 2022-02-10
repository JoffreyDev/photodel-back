from django.db import models
from accounts.models import Profile
from django.utils import timezone


class Chat(models.Model):
    sender_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')

    def __str__(self):
        return f'{self.pk}'


class Message(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author_message')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    status_read = models.BooleanField(default=False)
