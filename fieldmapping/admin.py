from django.contrib import admin
from django.utils import timezone
from .models import Location, Farm, Crop

class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set date_created if the object is being created
            obj.date_created = timezone.now()
        obj.save()


admin.site.register(Location, LocationAdmin)
admin.site.register(Farm)
admin.site.register(Crop)