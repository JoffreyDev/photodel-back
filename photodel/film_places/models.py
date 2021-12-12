from django.db import models
from django.contrib.gis.db import models as gis_models
from accounts.models import Profile


class CategoryFilmPlaces(models.Model):
    name_category = models.CharField(max_length=40)


class FilmPlaces(models.Model):
    name_place = models.CharField(max_length=50)
    # place_image = models

    city = models.CharField(max_length=40, blank=True)
    place_location = gis_models.PointField(srid=4326)
    category = models.ForeignKey(CategoryFilmPlaces, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Favorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.ForeignKey(FilmPlaces, on_delete=models.CASCADE)
