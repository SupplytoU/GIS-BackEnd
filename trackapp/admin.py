from django.contrib import admin
from django import forms
from .models import Vehicle, Driver, Route, Trip, TripLog
from fieldmapping.models import Location

admin.site.register(Vehicle)
admin.site.register(Driver)


class RouteAdminForm(forms.ModelForm):
    origin = forms.ModelChoiceField(queryset=Location.objects.all(), to_field_name='name')
    destination = forms.ModelChoiceField(queryset=Location.objects.all(), to_field_name='name')

    class Meta:
        model = Route
        fields = ['origin', 'destination']

class RouteAdmin(admin.ModelAdmin):
    form = RouteAdminForm
    readonly_fields = ('distance',)

admin.site.register(Route, RouteAdmin)

admin.site.register(Trip)
admin.site.register(TripLog)
