# Generated by Django 3.2.7 on 2022-10-21 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('additional_entities', '0012_alter_advertisement_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='end',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='note',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='start',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='status',
        ),
        migrations.RemoveField(
            model_name='customsettings',
            name='current_ad',
        ),
    ]