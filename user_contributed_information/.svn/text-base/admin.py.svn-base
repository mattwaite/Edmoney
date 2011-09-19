from django.contrib import admin
from stimulustracker.user_contributed_information.models import Contributor, Contribution
 
class ContributorAdmin(admin.ModelAdmin):
    search_fields = ['username']

admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Contribution)