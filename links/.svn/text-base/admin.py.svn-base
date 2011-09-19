from django.contrib import admin
from stimulustracker.links.models import Link

class LinkAdmin(admin.ModelAdmin):
    raw_id_fields = ['states_tagged', 'districts_tagged', 'schools_tagged']
    list_display = ['link_title', 'active']
    list_editable = ['active']
    class Media:
       js = ('/media/js/tiny_mce/tiny_mce.js',
             '/media/js/tiny_mce/textareas.js',)

admin.site.register(Link, LinkAdmin)
