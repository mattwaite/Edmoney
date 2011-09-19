from stimulustracker.stimulus.models import PrimaryAward, SecondaryAward
from django.shortcuts import get_object_or_404, render_to_response

def primary_detail(request, primarystimid):
    award = get_object_or_404(PrimaryAward, arra_id=primarystimid)
    return render_to_response('stimulus/primary_stimulus_detail.html', {
        'award': award,
    })

def secondary_detail(request, secondarystimid):
    award = get_object_or_404(SecondaryAward, id=secondarystimid)
    return render_to_response('stimulus/secondary_stimulus_detail.html', {
        'award': award,
    })