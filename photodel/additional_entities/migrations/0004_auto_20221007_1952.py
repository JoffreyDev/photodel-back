# Generated by Django 3.2.7 on 2022-10-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional_entities', '0003_alter_advertisement_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='minutes_to_show',
        ),
        migrations.AddField(
            model_name='customsettings',
            name='count_minutes_advert_show',
            field=models.IntegerField(default=5),
        ),
    ]
