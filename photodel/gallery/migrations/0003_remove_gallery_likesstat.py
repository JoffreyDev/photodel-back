# Generated by Django 3.2.7 on 2022-10-21 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_gallery_likesstat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='likesStat',
        ),
    ]