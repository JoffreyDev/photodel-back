# Generated by Django 3.2.7 on 2022-10-11 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film_places', '0002_filmplaces_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmplaces',
            old_name='likes',
            new_name='likesStat',
        ),
    ]