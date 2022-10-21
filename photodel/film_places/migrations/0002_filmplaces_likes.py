# Generated by Django 3.2.7 on 2022-10-11 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmplaces',
            name='likes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
