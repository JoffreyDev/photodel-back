# Generated by Django 3.2.7 on 2022-05-18 12:35

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('avatar', models.ImageField(
                    default='default_images/anonymous.jpg', upload_to='avatars/')),
                ('date_register', models.DateTimeField(
                    default=django.utils.timezone.localtime)),
                ('last_date_in', models.DateTimeField(blank=True, null=True)),
                ('last_ip', models.CharField(blank=True, max_length=15)),
                ('work_condition', models.CharField(blank=True, max_length=100)),
                ('cost_services', models.CharField(blank=True, max_length=100)),
                ('photo_technics', models.CharField(blank=True, max_length=50)),
                ('about', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(default=1)),
                ('pay_status', models.IntegerField(default=0)),
                ('ready_status', models.CharField(blank=True, choices=[
                 ('BUSY', 'Занят'), ('FREE', 'Свободен')], max_length=50)),
                ('pro_account', models.IntegerField(default=1, null=True)),
                ('expired_pro_subscription',
                 models.DateTimeField(blank=True, null=True)),
                ('rating', models.IntegerField(default=0, validators=[
                 django.core.validators.MinValueValidator(0)])),
                ('location', django.contrib.gis.db.models.fields.PointField(
                    blank=True, null=True, srid=4326)),
                ('string_location', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('site', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('email_verify', models.BooleanField(default=False)),
                ('instagram', models.CharField(blank=True, max_length=40)),
                ('facebook', models.CharField(blank=True, max_length=40)),
                ('vk', models.CharField(blank=True, max_length=40)),
                ('location_now', django.contrib.gis.db.models.fields.PointField(
                    blank=True, null=True, srid=4326)),
                ('string_location_now', models.CharField(
                    blank=True, max_length=50, null=True)),
                ('date_stay_start', models.DateTimeField(blank=True, null=True)),
                ('date_stay_end', models.DateTimeField(blank=True, null=True)),
                ('message', models.TextField(blank=True)),
                ('is_adult', models.BooleanField(default=False)),
                ('is_show_nu_photo', models.BooleanField(default=False)),
                ('is_hide', models.BooleanField(default=False)),
                ('is_change', models.BooleanField(default=False)),
                ('is_confirm', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0, validators=[
                 django.core.validators.MinValueValidator(0)])),
                ('last_views', models.IntegerField(default=0, validators=[
                 django.core.validators.MinValueValidator(0)])),
                ('user_channel_name', models.CharField(
                    blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name_spec', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('email_code', models.CharField(
                    blank=True, max_length=30, null=True)),
                ('password_reset_token', models.CharField(
                    blank=True, max_length=30, null=True)),
                ('profile_id', models.OneToOneField(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='receiver_like', to='accounts.profile')),
                ('sender_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='sender_like', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='receiver_favorite', to='accounts.profile')),
                ('sender_favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='sender_favorite', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(
                    default=django.utils.timezone.localtime)),
                ('answer_id_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                 related_name='profile_comment_answer', to='accounts.profilecomment')),
                ('quote_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                 related_name='profile_comment_quote', to='accounts.profilecomment')),
                ('receiver_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='receiver_comment', to='accounts.profile')),
                ('sender_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='sender_comment', to='accounts.profile')),
            ],
        ),
    ]
