from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('locations/', views.LocationList.as_view(), name='locations'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='location-detail'),
    path('locations/<str:label>/', views.LocationLabelTypeView.as_view(), name='location-type'),
    path('farms/', views.FarmList.as_view(), name='farms'),
    path('farms/<int:pk>/', views.FarmDetail.as_view(), name='farm-detail'),
    path('produce/', views.ProduceList.as_view(), name='produce'),
    path('farmers/', views.FarmerList.as_view(), name='farmers')
]

urlpatterns = format_suffix_patterns(urlpatterns)