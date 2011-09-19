from django.contrib import admin
from stimulustracker.ugc.models import Contributor, Contribution
 
class ContributorAdmin(admin.ModelAdmin):
    search_fields = ['username']
    
class ContributionAdmin(admin.ModelAdmin):
    search_fields = ['comment']        

admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Contribution, ContributionAdmin)