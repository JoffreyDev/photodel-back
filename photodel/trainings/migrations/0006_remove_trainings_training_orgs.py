# Generated by Django 3.2.7 on 2022-12-22 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0005_auto_20221223_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainings',
            name='training_orgs',
        ),
    ]
