from stimulustracker.user_contributed_information.models import Contribution
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def contribution_detail(request, contribid):
    contribution = get_object_or_404(Contribution, id=contribid)
    return render_to_response('usercontributions/contribution_detail.html', {
        'contribution': contribution,
    },
        context_instance=RequestContext(request))