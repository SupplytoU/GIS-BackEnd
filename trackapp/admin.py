from django.contrib import admin
from .models import Vehicle, Driver, Route, Trip, TripLog

admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(TripLog)
