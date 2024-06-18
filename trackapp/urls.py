from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('routes/', RouteCreateListView.as_view(), name='routes'),
    path('routes/<int:pk>/', RouteDetailView.as_view(), name='route-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)