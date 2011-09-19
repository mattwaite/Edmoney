#!/usr/bin/env python
from django.contrib import admin
from stimulustracker.specials.models import SpecialReport

class SpecialReportAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name',)}
    class Media:
       js = ('/media/js/tiny_mce/tiny_mce.js',
             '/media/js/tiny_mce/textareas.js',)

admin.site.register(SpecialReport, SpecialReportAdmin)
