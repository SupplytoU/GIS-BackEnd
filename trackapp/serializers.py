from rest_framework import serializers
from .models import Vehicle, Driver, Route, Trip, TripLog
from fieldmapping.models import Location


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'number_plate', 'vehicle_type']


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'license_number', 'phone_number', 'vehicle']


class RouteSerializer(serializers.ModelSerializer):
    origin = serializers.SlugRelatedField(slug_field='name', queryset=Location.objects.all())
    destination = serializers.SlugRelatedField(slug_field='name', queryset=Location.objects.all())

    class Meta:
        model = Route
        fields = ['id', 'origin', 'destination', 'distance']
        read_only_fields = ['distance']


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'vehicle', 'driver', 'start_time', 'end_time', 'status']


class TripLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripLog
        fields = ['id', 'trip', 'time_stamp', 'location', 'remarks']
