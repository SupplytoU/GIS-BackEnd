
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('users.urls')),
    path('api/fieldmapping/', include('fieldmapping.urls')),
    path('api/trachapp/', include('trackapp.urls'))
    
]
