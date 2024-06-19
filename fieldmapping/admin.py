from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from django.utils import timezone
from .models import Location, Farm, Farmer, Produce


class CustomLocationAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    readonly_fields = ('date_created',)
    change_list_template = 'admin/fieldmapping/location/location_change_list.html'
    change_form_template = 'admin/fieldmapping/location/change_form.html'
    list_filter = ('region', 'label')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.date_created = timezone.now()
        obj.save()

    def changelist_view(self, request, extra_context=None):
        locations = Location.objects.all()
        location_data = [
            {
                'name': loc.name,
                'label': loc.label,
                'lat': loc.location.y,
                'lng': loc.location.x,
            }
            for loc in locations
        ]

        extra_context = extra_context or {}
        extra_context['locations'] = location_data

        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Location, CustomLocationAdmin)


class CustomFarmAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_display = ('name', 'location', 'farmer')
    list_filter = ('produce', 'farmer')
    filter_horizontal = ('produce',)
    change_list_template = 'admin/fieldmapping/farm/farm_change_list.html'

    def changelist_view(self, request, extra_context=None):
        farms = Farm.objects.all()
        farm_data = []
        for farm in farms:
            # Assuming 'polygon' is the field name for the farm's polygon
            geojson = farm.farm_area.geojson if farm.farm_area else None
            farm_data.append({
                'name': farm.name,
                'geojson': geojson
            })

        extra_context = extra_context or {}
        extra_context['farms'] = farm_data

        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Farm, CustomFarmAdmin)
admin.site.register(Produce)
admin.site.register(Farmer)
