from rest_framework import serializers
from .models import Location, Farm, Farmer, Produce

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name' , 'label' , 'location', 'description', 'date_created']


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['id', 'name', 'phone_number']
    

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['id', 'name' , 'farm_area' , 'description', 'region', 'location', 'produce']


class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = ['id', 'produce_type', 'variety', 'description']