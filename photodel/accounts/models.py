from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from additional_entities.models import Country, Language
from rest_framework.exceptions import ValidationError
from rest_framework import serializers


class GalleryImage(models.Model):
    photo = models.ImageField(upload_to='gallery/')


class Specialization(models.Model):
    name_spec = models.CharField(max_length=50)

    def __str__(self):
        return self.name_spec


class ProCategory(models.Model):
    name_category = models.CharField(max_length=50)

    def __str__(self):
        return self.name_category


class Profile(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/anonymous.jpg')
    date_register = models.DateTimeField(default=timezone.localtime)
    last_date_in = models.DateTimeField(null=True, blank=True)
    last_ip = models.CharField(max_length=15, blank=True)
    filming_geo = models.ManyToManyField(Country, blank=True)
    work_condition = models.CharField(max_length=100, blank=True)
    cost_services = models.CharField(max_length=100, blank=True)
    photo_technics = models.CharField(max_length=50, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    about = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=1)  # 1 - Клиент 2 - Профи
    ready_status = models.CharField(max_length=50, blank=True)
    type_pro = models.ForeignKey(ProCategory, on_delete=models.CASCADE, null=True, blank=True)
    spec_model_or_photographer = models.ManyToManyField(Specialization, blank=True)
    type_pro_account = models.IntegerField(default=1, null=True)  # 1 - Бесплатный 2 - Стандарт 3 - Максимум
    expired_pro_subscription = models.DateTimeField(blank=True, null=True)

    # contacts
    location = gis_models.PointField(srid=4326, blank=True, null=True)
    string_location = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, blank=True)
    site = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=50)
    email_verify = models.BooleanField(default=False)
    instagram = models.CharField(max_length=40, blank=True)
    facebook = models.CharField(max_length=40, blank=True)
    vk = models.CharField(max_length=40, blank=True)

    # temporary geolocation
    location_now = gis_models.PointField(srid=4326, blank=True, null=True)
    string_location_now = models.CharField(max_length=50, null=True)
    date_stay_start = models.DateTimeField(blank=True, null=True)
    date_stay_end = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True)

    is_adult = models.BooleanField(default=False)
    is_show_nu_photo = models.BooleanField(default=False)
    is_hide = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if (self.type_pro.name_category != 'Модели' and self.type_pro.name_category != 'Фотографы') \
                and self.spec_model_or_photographer.all():
            raise ValidationError({"error": "Вы не являетесь моделью или фотографом для выбора специализации"})
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Album(models.Model):
    name_album = models.CharField(max_length=40)
    description_album = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Gallery(models.Model):
    gallery_image = models.ForeignKey(GalleryImage, on_delete=models.CASCADE)
    name_image = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    place_location = gis_models.PointField(srid=4326)
    photo_camera = models.CharField(max_length=40)
    focal_len = models.CharField(max_length=40)
    excerpt = models.CharField(max_length=40)
    flash = models.CharField(max_length=40)
    last_ip_user = models.CharField(max_length=18, null=True, blank=True)
    views = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    # category = models.ForeignKey(GalleryImages, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_image


class GalleryComment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    sender_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class GalleryLike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class GalleryFavorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class VerificationCode(models.Model):
    profile_id = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    email_code = models.CharField(max_length=30, blank=True, null=True)
    password_reset_token = models.CharField(max_length=30, blank=True, null=True)


