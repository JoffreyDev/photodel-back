# Generated by Django 3.2.7 on 2022-10-21 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film_places', '0005_filmplaces_likesstat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmplaces',
            old_name='likesStat',
            new_name='likes_stat',
        ),
    ]
