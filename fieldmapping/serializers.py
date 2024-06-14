from rest_framework import serializers
from .models import Location, Farm, Farmer, Produce


class LocationSerializer(serializers.ModelSerializer):
    date_created = serializers.ReadOnlyField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'label', 'location', 'description', 'date_created']


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['name', 'phone_number']


class ProduceSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)

            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Produce
        fields = ['id', 'produce_type', 'variety', 'description']


class FarmSerializer(serializers.ModelSerializer):
    area = serializers.SerializerMethodField()
    produce = serializers.SerializerMethodField()

    class Meta:
        model = Farm
        fields = ['name', 'farm_area', 'area', 'description', 'region', 'location', 'produce', 'farmer']

    def get_area(self, obj):
        return obj.calculate_area

    def get_produce(self, obj):
        produce = obj.produce.all()
        serializer = ProduceSerializer(produce, many=True, fields=['produce_type', 'variety'])
        return serializer.data

