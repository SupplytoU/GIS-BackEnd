from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from django.utils import timezone
from .models import Location, Farm, Farmer, Produce


class CustomLocationAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    readonly_fields = ('date_created',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.date_created = timezone.now()
        obj.save()


admin.site.register(Location, CustomLocationAdmin)


class CustomFarmAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_display = ('name', 'region', 'location', 'farmer')
    list_filter = ('region', 'produce')
    filter_horizontal = ('produce',)


admin.site.register(Farm, CustomFarmAdmin)
admin.site.register(Produce)
admin.site.register(Farmer)
