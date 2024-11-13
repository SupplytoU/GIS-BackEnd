from django.db import models
from django.contrib.gis.db import models as gis_models
from django.utils import timezone


# Create your models here.


class Farmer(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Farmers'


class Produce(models.Model):
    produce_type = models.CharField(max_length=100)
    variety = models.CharField(max_length=225, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.variety:
            return f'{self.produce_type} variety: {self.variety}'
        else:
            return f'{self.produce_type}'

    class Meta:
        verbose_name_plural = 'Crops'


class Farm(models.Model):
    name = models.CharField(max_length=100)
    farm_area = gis_models.PolygonField(srid=4326)
    area_acres = models.FloatField()
    description = models.TextField(blank=True, null=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='farms')
    produce = models.ManyToManyField(Produce, related_name='farms')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Farms'


class Location(models.Model):
    LABEL_CHOICES = [
        ('farms', 'Farm'),
        ('processing-facilities', 'Processing Facility'),
        ('distribution-centers', 'Distribution Center'),
        ('warehouses', 'Warehouse'),
        ('restaurants', 'Restaurant'),
        ('supermarkets', 'Supermarket')
    ]
    REGION_CHOICES = [
        ('central', 'Central'),
        ('coast', 'Coast'),
        ('eastern', 'Eastern'),
        ('nairobi', 'Nairobi'),
        ('north-eastern', 'North Eastern'),
        ('nyanza', 'Nyanza'),
        ('rift-valley', 'Rift Valley'),
        ('western', 'Western')
    ]
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100, choices=LABEL_CHOICES)
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(default=timezone.now)
    location = gis_models.PointField(srid=4326)
    farm = models.OneToOneField(Farm, on_delete=models.CASCADE, related_name='location', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Locations'
