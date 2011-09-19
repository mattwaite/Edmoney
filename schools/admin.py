from django.contrib.gis import admin
from stimulustracker.schools.models import SchoolType, SchoolStatus, DistrictType, DistrictStatus, StateEducationDepartment, District, School
 
class SchoolTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'school_type_slug': ('school_type',)}
    
class StateEducationDepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'state_name_slug': ('state_name',)}
     
class DistrictAdmin(admin.ModelAdmin):
    prepopulated_fields = {'district_name_slug': ('district_name',)}
    search_fields = ['district_name']
    list_display = ['district_name', 'state']
    list_filter = ['state']
    
class SchoolAdmin(admin.GeoModelAdmin):
    prepopulated_fields = {'school_name_slug': ('school_name',)}
    search_fields = ['school_name']
    list_display = ['school_name', 'city', 'state']
    raw_id_fields = ['district']    
        
admin.site.register(SchoolType, SchoolTypeAdmin)
admin.site.register(SchoolStatus)
admin.site.register(DistrictType)
admin.site.register(DistrictStatus)
admin.site.register(StateEducationDepartment, StateEducationDepartmentAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(School, SchoolAdmin)
