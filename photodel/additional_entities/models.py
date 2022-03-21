from django.db import models


class EmailFragment(models.Model):
    verify_email = models.TextField(null=True)
    reset_password = models.TextField(null=True)


class CustomSettings(models.Model):
    distance_for_unique_places = models.IntegerField()


class Country(models.Model):
    name_country = models.CharField(max_length=45)


class Language(models.Model):
    name_language = models.CharField(max_length=15)


class Advertisement(models.Model):
    ad_image = models.ImageField(upload_to='ad/')
    ad_title = models.CharField(max_length=255)
    ad_link = models.CharField(max_length=255)
    ad_count_click = models.IntegerField(default=0)


class BanWord(models.Model):
    word = models.CharField(max_length=45)
