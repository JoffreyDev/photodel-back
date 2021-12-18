from django.db import models


class EmailFragment(models.Model):
    verify_email = models.TextField(null=True)
    reset_password = models.TextField(null=True)


class CustomSettings(models.Model):
    distance_for_unique_places = models.IntegerField()


class Country(models.Model):
    name_country = models.CharField(max_length=45)