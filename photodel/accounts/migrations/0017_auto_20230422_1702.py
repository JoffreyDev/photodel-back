# Generated by Django 3.2.7 on 2023-04-22 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20230422_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='expired_pro_subscription',
            new_name='pro_subscription_expiration',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pro_expiration',
        ),
    ]
