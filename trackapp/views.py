from rest_framework import generics, permissions
from .serializers import RouteSerializer
from .models import *


class RouteCreateListView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer



class RouteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

