# Generated by Django 3.2.7 on 2022-10-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional_entities', '0014_auto_20221021_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='customsettings',
            name='current_ad',
            field=models.IntegerField(default=1),
        ),
    ]
