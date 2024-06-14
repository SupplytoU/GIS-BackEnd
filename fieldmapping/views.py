from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location, Farm, Produce
from .serializers import LocationSerializer, FarmSerializer, ProduceSerializer
from django.utils import timezone
from django.shortcuts import get_object_or_404


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
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        


class FarmList(generics.ListCreateAPIView):
    """
    List all locations or create a new location
    """
    serializer_class = FarmSerializer
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        """
        Return all farms or filter them by region, produce
        """
        queryset = Farm.objects.all()
        region = self.request.query_params.get('region')
        produce= self.request.query_params.get('produce')

        if region:
            queryset = queryset.filter(region=region)

        if produce:
            produce_type = get_object_or_404(Produce, produce_type=produce)
            queryset = queryset.filter(produce=produce_type)

        return queryset

    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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

