from django.db import models
from django.utils import timezone


class EmailFragment(models.Model):
    verify_email = models.TextField(null=True)
    reset_password = models.TextField(null=True)


class CustomSettings(models.Model):
    distance_for_unique_places = models.IntegerField()


class Country(models.Model):
    name_country = models.CharField(max_length=45)

    def __str__(self):
        return self.name_country


class Language(models.Model):
    name_language = models.CharField(max_length=15)


class Advertisement(models.Model):
    ad_image = models.ImageField(upload_to='ad/')
    ad_title = models.CharField(max_length=255)
    ad_link = models.CharField(max_length=255)
    ad_count_click = models.IntegerField(default=0)


class BanWord(models.Model):
    word = models.CharField(max_length=45)


class City(models.Model):
    city_name = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Question(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Answer(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return self.choice.title
