from rest_framework import serializers
from .models import Location, Farm, Crop

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name' , 'label' , 'location', 'description']
    

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['id', 'name' , 'farm_area' , 'description', 'region', 'location']


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['id', 'name' , 'crop_type' , 'description', 'farm']