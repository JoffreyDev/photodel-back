from django.db import models
from django.contrib.gis.db import models as gis_models
from accounts.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator


class PlaceImages(models.Model):
    photo = models.ImageField(upload_to='places/')


class CategoryFilmPlaces(models.Model):
    name_category = models.CharField(max_length=40)


class FilmPlaces(models.Model):
    name_place = models.CharField(max_length=50)
    place_image = models.ManyToManyField(PlaceImages)
    description = models.TextField(blank=True)
    photo_camera = models.CharField(max_length=40)
    cost = models.FloatField(validators=[MinValueValidator(0.0)])
    payment = models.CharField(max_length=40)
    place_location = gis_models.PointField(srid=4326)
    views = models.IntegerField(default=0, validators=[MinValueValidator(0.0)])
    category = models.ManyToManyField(CategoryFilmPlaces)
    rel_object = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)
    is_main = models.BooleanField(default=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Favorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.ForeignKey(FilmPlaces, on_delete=models.CASCADE)
