from django.core.exceptions import MultipleObjectsReturned
from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location, Farm, Produce, Farmer
from .serializers import LocationSerializer, FarmSerializer, ProduceSerializer, FarmerSerializer


class LocationList(generics.ListCreateAPIView):
    """
    List all locations or create a new location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]


class LocationLabelTypeView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, label, *args, **kwargs):
        """
        filters the different types of locations
        """
        location_type = Location.objects.filter(label=label)
        if location_type.exists():
            serializer = LocationSerializer(location_type, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No locations found with that label'}, status=status.HTTP_404_NOT_FOUND)


class FarmList(generics.ListCreateAPIView):
    """
    List all locations or create a new location
    """
    serializer_class = FarmSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Return all farms or filter them by region, produce. Return 404 if no matching farms are found.
        """
        queryset = Farm.objects.all()
        region = self.request.query_params.get('region')
        produce = self.request.query_params.get('produce')

        if region:
            if not Farm.objects.filter(region=region).exists():
                raise NotFound('No farm in the reqion {}'.format(region))
            queryset = queryset.filter(region=region)

        if produce:
            try:
                produce_type = Produce.objects.get(produce_type=produce)
                queryset = queryset.filter(produce=produce_type)
            except Produce.DoesNotExist:
                raise NotFound("No produce found with that type.")
            except MultipleObjectsReturned:
                produce_objects = Produce.objects.filter(produce_type=produce)
                if produce_objects.exists():
                    queryset = queryset.filter(produce__in=produce_objects)
                else:
                    raise NotFound("No produce found with that type.")

        if not queryset.exists():
            raise NotFound("No farms found with the given criteria.")

        return queryset

    def perform_create(self, serializer):
        produce_data = self.request.data.pop('produce', None)

        farm = serializer.save()

        if produce_data:
            for produce_item in produce_data:
                produce_serializer = ProduceSerializer(data=produce_item)
                produce_serializer.is_valid(raise_exception=True)
                produce = produce_serializer.save()
                farm.produce.add(produce)


class FarmDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a farm
    """
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.AllowAny]


class ProduceList(generics.ListCreateAPIView):
    """
    List all produce or create a new produce
    """
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer
    permission_classes = [permissions.AllowAny]


class FarmerList(generics.ListCreateAPIView):
    """
    List all farmers or create a new farmer
    """
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [permissions.AllowAny]
