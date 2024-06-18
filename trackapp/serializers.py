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
    origin = serializers.CharField(source='get_origin_display')
    destination = serializers.CharField(source='get_destination_display')

    class Meta:
        model = Route
        fields = ['id', 'origin', 'destination', 'distance']

    def __init__(self, *args, **kwargs):
        super(RouteSerializer, self).__init__(*args, **kwargs)
        locations = Location.objects.all()
        choices = [(location.location, location.name) for location in locations]
        self.fields['origin'].choices = choices
        self.fields['destination'].choices = choices

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['origin'] = Location.objects.get(location=instance.origin).name
        representation['destination'] = Location.objects.get(location=instance.destination).name
        return representation

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['origin'] = Location.objects.get(name=data['origin']).location
        internal_value['destination'] = Location.objects.get(name=data['destination']).location
        return internal_value


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'vehicle', 'driver', 'route', 'start_time', 'end_time', 'status']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripLog
        fields = ['id', 'trip', 'time_stamp', 'location', 'remarks']