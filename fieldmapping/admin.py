from django.contrib import admin
from django.utils import timezone
from .models import Location, Farm, Produce, Farmer

class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set date_created if the object is being created
            obj.date_created = timezone.now()
        obj.save()


admin.site.register(Location, LocationAdmin)

class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'location', 'farmer')
    list_filter = ('region',)

admin.site.register(Farm, FarmAdmin)
admin.site.register(Produce)
admin.site.register(Farmer)