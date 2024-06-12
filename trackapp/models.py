from django.db import models
from django.contrib.gis.db import models as gis_models

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('pickup','Pickup'),
        ('canter','Canter'),
        ('lorry','Lorry'),
        ('trailer', 'Trailer')
    ]
    number_plate = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)



class Driver(models.Model):
    name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def _str_(self):
        return f'{self.name}'


class Route(models.Model):
    origin = gis_models.PointField()
    destination = gis_models.PointField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)


class Trip(models.Model):
    TRIP_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=TRIP_STATUS_CHOICES)


class TripLog(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    location = gis_models.PointField()
    remarks = models.TextField(blank=True)
