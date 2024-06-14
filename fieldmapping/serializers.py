from rest_framework import serializers
from .models import Location, Farm, Farmer, Produce

class LocationSerializer(serializers.ModelSerializer):
    date_created = serializers.ReadOnlyField()
    class Meta:
        model = Location
        fields = ['id', 'name' , 'label' , 'location', 'description', 'date_created']


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['id', 'name', 'phone_number']


class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = ['id', 'produce_type', 'variety']    

class FarmSerializer(serializers.ModelSerializer):
    area = serializers.ReadOnlyField()
    produce = ProduceSerializer(many=True)
    class Meta:
        model = Farm
        fields = ['id', 'name' , 'farm_area' , 'area', 'description', 'region', 'location', 'produce']

    
    def get_area(self, obj):
        return obj.calculate_area()


