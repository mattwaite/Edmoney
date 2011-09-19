from django.contrib import admin
from stimulustracker.demographics.models import SchoolDemographics, DistrictDemographics

class SchoolDemographicsAdmin(admin.ModelAdmin):
    raw_id_fields = ['school']
    search_fields = ['school__school_name']

admin.site.register(SchoolDemographics, SchoolDemographicsAdmin)
admin.site.register(DistrictDemographics)