from django.contrib.gis import admin
from stimulustracker.geography.models import State, County, City, Zipcode, CongressionalDistrict

class StateAdmin(admin.ModelAdmin):
    list_display = ['state_name', 'state_abbreviation']
    list_editable = ['state_abbreviation']

admin.site.register(State, StateAdmin)
admin.site.register(County)
admin.site.register(City)
admin.site.register(Zipcode)
admin.site.register(CongressionalDistrict)