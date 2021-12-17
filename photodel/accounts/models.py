from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User


class Specialization(models.Model):
    TYPE_MODEL_CHOICE = [
        ('1', 'Взрослые Мужчина'),
        ('2', 'Взрослые Женщина'),
        ('3', 'Дети Мальчики'),
        ('4', 'Дети Девочки'),
    ]

    name_spec = models.CharField(max_length=50)
    type_model = models.CharField(max_length=20, choices=TYPE_MODEL_CHOICE, blank=True)

    def __str__(self):
        return self.name_spec


class ProCategory(models.Model):
    name_category = models.CharField(max_length=50)
    spec_model_or_photographer = models.ManyToManyField(Specialization, blank=True)

    def __str__(self):
        return self.name_category


class Profile(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_register = models.DateTimeField(default=timezone.localtime)
    last_date_in = models.DateTimeField(null=True, blank=True)
    last_ip = models.CharField(max_length=15, blank=True)
    filming_geo = models.CharField(max_length=100, blank=True)
    work_condition = models.CharField(max_length=100, blank=True)
    cost_services = models.CharField(max_length=100, blank=True)
    photo_technics = models.CharField(max_length=50, blank=True)
    languages = models.CharField(max_length=255, blank=True)
    about = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=1)  # 1 - Клиент 2 - Профи
    type_pro = models.ForeignKey(ProCategory, on_delete=models.CASCADE, null=True, blank=True)
    type_pro_account = models.IntegerField(default=1, null=True)  # 1 - Бесплатный 2 - Стандарт 3 - Максимум
    expired_pro_subscription = models.DateTimeField(blank=True, null=True)

    # contacts
    location = gis_models.PointField(srid=4326, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    site = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=50)
    email_verify = models.BooleanField(default=False)
    instagram = models.CharField(max_length=40, blank=True)
    facebook = models.CharField(max_length=40, blank=True)
    vk = models.CharField(max_length=40, blank=True)

    # temporary geolocation
    location_now = gis_models.PointField(srid=4326, blank=True, null=True)
    date_stay_start = models.DateTimeField(blank=True, null=True)
    date_stay_end = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True)

    is_adult = models.BooleanField(default=False)
    is_show_nu_photo = models.BooleanField(default=False)
    is_hide = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class VerificationCode(models.Model):
    profile_id = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    email_code = models.CharField(max_length=30, blank=True, null=True)
    password_reset_token = models.CharField(max_length=30, blank=True, null=True)


