from django.contrib import admin
from stimulustracker.stimulus.models import Agency, AwardType, PrimaryAward, SecondaryAward

class AgencyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'agency_name_slug': ('agency_name',)}

class AwardTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'award_type_slug': ('award_type',)}

class PrimaryAwardAdmin(admin.ModelAdmin):
    search_fields = ['recipient_name', ]
    list_display = ['recipient_name', 'clean_short_name', 'state_funded', 'district_funded', 'school_funded']
    list_filter = ['recipient_state']
    raw_id_fields = ['state_funded', 'district_funded', 'school_funded']

class SecondaryAwardAdmin(admin.ModelAdmin):
    search_fields = ['recipient_name', ]
    raw_id_fields = ['primary_award', 'state_funded', 'district_funded', 'school_funded']
    list_display = ['recipient_name', 'state_funded', 'district_funded', 'amount_awarded']
    list_filter = ['recipient_state']
    list_editable = ['district_funded']

admin.site.register(Agency, AgencyAdmin)
admin.site.register(AwardType, AwardTypeAdmin)
admin.site.register(PrimaryAward, PrimaryAwardAdmin)
admin.site.register(SecondaryAward, SecondaryAwardAdmin)
