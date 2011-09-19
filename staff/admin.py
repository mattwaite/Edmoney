from django.contrib import admin
from stimulustracker.staff.models import Staffer
 
class StafferAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('first_name','last_name')}
    class Media:
       js = ('/media/js/tiny_mce/tiny_mce.js',
             '/media/js/tiny_mce/textareas.js',)
        
admin.site.register(Staffer, StafferAdmin)