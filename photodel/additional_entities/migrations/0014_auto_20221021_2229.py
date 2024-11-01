# Generated by Django 3.2.7 on 2022-10-21 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('additional_entities', '0013_auto_20221021_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='note',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
