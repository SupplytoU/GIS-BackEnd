from rest_framework import serializers
from .models import Location, Farm, Produce, Farmer

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name' , 'label' , 'location', 'description']


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['id', 'name', 'phone_number']
    

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['id', 'name' , 'farm_area' , 'description', 'region', 'location']


class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = ['id', 'produce_type', 'variety', 'description', 'farm']