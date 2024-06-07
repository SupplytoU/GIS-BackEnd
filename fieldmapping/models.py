from django.db import models
from django.contrib.gis.db import models as gis_models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    location = gis_models.PointField(srid=4326)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Locations'

class Farm(models.Model):
    name = models.CharField(max_length=100)
    farm_area =gis_models.PolygonField(srid=4326)
    description = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='farms')
    

    def _str_(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Farms'


class Crop(models.Model):
    name = models.CharField(max_length=100)
    type= models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='crops')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Crops'   