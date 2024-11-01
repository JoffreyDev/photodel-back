# Generated by Django 3.2.7 on 2023-02-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_notifications_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='type',
            field=models.CharField(choices=[('NEW_SESSION_LIKE', 'новый лайк фотосессии'), ('NEW_SESSION_COMMENT', 'новый комментарий к фотосессии'), ('NEW_SESSION_FAVORITE', 'новое добавление фотосессии в избранное'), ('NEW_PHOTO_LIKE', 'новый лайк фотографии'), ('NEW_PHOTO_COMMENT', 'новый комментарий к фотографии'), ('NEW_PHOTO_FAVORITE', 'новое добавление фотографии в избранное'), ('NEW_PLACE_LIKE', 'новый лайк места для съемки'), ('NEW_PLACE_COMMENT', 'новый комментарий к месту для съемки'), ('NEW_PLACE_FAVORITE', 'новое добавление места для съемки в избранное'), ('NEW_TRAINING_LIKE', 'новый лайк обучения'), ('NEW_TRAINING_COMMENT', 'новый комментарий к обучению'), ('NEW_TRAINING_FAVORITE', 'новое добавление обучения в избранное'), ('NEW_MESSAGE', 'новое сообщение'), ('NEW_FILMING_REQUEST', 'новый запрос на съемку'), ('NEW_TRAINING_REQUEST', 'новый запрос на обучение'), ('NEW_TEAM_REQUEST', 'новый запрос в команду'), ('NEW_REVIEW', 'новый отзыв')], max_length=25),
        ),
    ]
