from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Point


# Create your models here.
class SOS(models.Model):
    category = models.CharField(max_length=255, default=None)
    image = models.ImageField(upload_to='photos', max_length=255)
    longitude = models.DecimalField(max_digits=16, decimal_places=6, default=0.0)
    latitude = models.DecimalField(max_digits=16, decimal_places=6, default=0.0)


