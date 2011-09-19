from stimulustracker.specials.models import SpecialReport
from django.shortcuts import render_to_response, get_object_or_404

def specials_detail(request, special):
    special_report = get_object_or_404(SpecialReport, name_slug=special)
    return render_to_response('specials/specials_main.html', {
        'special_report': special_report,
    })