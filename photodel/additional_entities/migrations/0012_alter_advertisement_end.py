# Generated by Django 3.2.7 on 2022-10-20 22:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('additional_entities', '0011_alter_advertisement_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]
