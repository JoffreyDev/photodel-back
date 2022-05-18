# Generated by Django 3.2.7 on 2022-05-18 07:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('film_places', '0001_initial'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sender_hide_chat', models.BooleanField(default=False)),
                ('is_receiver_hide_chat', models.BooleanField(default=False)),
                ('receiver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='accounts.profile')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='RequestChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_receiver', to='accounts.profile')),
                ('request_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_sender', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='RequestMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.localtime)),
                ('status_read', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_author_message', to='accounts.profile')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.requestchat')),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_author_message', to='film_places.filmrequest')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_note', models.CharField(choices=[('MESSAGE', 'новое сообшение'), ('REQUEST', 'Новое запрос'), ('REQUEST_MESSAGE', 'Новое сообщение в запросе'), ('UPDATE_REQUEST', 'Обновление статуса запроса'), ('LIKE_PROFILE', 'Лайк профиля'), ('LIKE_PHOTO', 'Лайк фото'), ('LIKE_PHOTO_SESSION', 'Лайк фотосессии'), ('LIKE_PLACE', 'Лайк места'), ('FAVORITE_PROFILE', 'Избранное профиля'), ('FAVORITE_PHOTO', 'Избранное фото'), ('FAVORITE_PHOTO_SESSION', 'Избранное фотосессии'), ('FAVORITE_PLACE', 'Избранное места'), ('COMMENT_PROFILE', 'Коммент профиля'), ('COMMENT_PHOTO', 'Коммент фото'), ('COMMENT_PHOTO_SESSION', 'Коммент фотосессии'), ('COMMENT_PLACE', 'Коммент места')], max_length=25, null=True)),
                ('text_note', models.TextField(null=True)),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.localtime)),
                ('model_id', models.IntegerField()),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_receiver', to='accounts.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_sender', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.localtime)),
                ('status_read', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_message', to='accounts.profile')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chat')),
            ],
        ),
    ]
