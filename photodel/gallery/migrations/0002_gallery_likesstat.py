# Generated by Django 3.2.7 on 2022-10-20 22:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='likesStat',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
