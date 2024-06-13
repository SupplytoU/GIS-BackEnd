from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location, Farm, Produce
from .serializers import LocationSerializer, FarmSerializer, ProduceSerializer
from django.utils import timezone


class LocationList(generics.ListCreateAPIView):
    """
    List all locations or create a new location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        validated_data['date_created'] = timezone.now()
        serializer.save(owner=self.request.user)


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]


class LabelTypeView(APIView):
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
        Return all farms or filter them by region
        """
        queryset = Farm.objects.all()
        region = self.request.query_params.get('region')
        if region:
            queryset = queryset.filter(region=region)
        return queryset
    

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        serializer.save(owner=self.request.user)


class FarmDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a farm
    """
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.AllowAny]