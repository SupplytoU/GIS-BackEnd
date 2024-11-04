from rest_framework import serializers
from .models import Location, Farm, Farmer, Produce


class LocationSerializer(serializers.ModelSerializer):
    date_created = serializers.ReadOnlyField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'label', 'location', 'region', 'description', 'date_created']


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
    farmer = serializers.CharField()  # Accept farmer name as a string

    class Meta:
        model = Farm
        fields = ['name', 'farm_area', 'area', 'description', 'produce', 'farmer']

    def get_area(self, obj):
        return obj.calculate_area

    def get_produce(self, obj):
        produce = obj.produce.all()
        serializer = ProduceSerializer(produce, many=True, fields=['produce_type', 'variety'])
        return serializer.data

    def create(self, validated_data):
        farmer_name = validated_data.pop('farmer')  # Extract the farmer name from validated data
        try:
            # Look up the farmer instance by name
            farmer_instance = Farmer.objects.get(name=farmer_name)
            validated_data['farmer'] = farmer_instance  # Set the farmer instance
        except Farmer.DoesNotExist:
            raise serializers.ValidationError(f"Farmer with name '{farmer_name}' does not exist.")
        
        # Now create the Farm instance
        farm = Farm.objects.create(**validated_data)  # Create Farm instance
        return farm

    def update(self, instance, validated_data):
        farmer_name = validated_data.pop('farmer', None)  # Extract farmer name if provided
        if farmer_name:
            try:
                farmer_instance = Farmer.objects.get(name=farmer_name)
                validated_data['farmer'] = farmer_instance  # Set the farmer instance for update
            except Farmer.DoesNotExist:
                raise serializers.ValidationError(f"Farmer with name '{farmer_name}' does not exist.")
        
        return super().update(instance, validated_data)  # Call the parent update method

