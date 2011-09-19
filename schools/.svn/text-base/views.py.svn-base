from stimulustracker.schools.models import School, District, StateEducationDepartment
from stimulustracker.stimulus.models import PrimaryAward, SecondaryAward
from stimulustracker.blog.models import Post
from stimulustracker.links.models import Link
from stimulustracker.demographics.models import DistrictDemographics, SchoolDemographics
from stimulustracker.user_contributed_information.models import ContributionForm, Contribution
from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from django.db.models import Sum, Count
from django.template import RequestContext, loader, Context
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.contenttypes.models import ContentType

def schools_main(request):
    states = StateEducationDepartment.objects.all()
    total_dollars = PrimaryAward.objects.aggregate(Sum('amount_awarded'))
    districts_tracked = SecondaryAward.objects.exclude(district_funded=None).count()
    schools_tracked = PrimaryAward.objects.exclude(school_funded=None).count()
    return render_to_response('schools/schools_main.html', {
        'states': states,
        'total_dollars': total_dollars,
        'districts_tracked': districts_tracked,
        'schools_tracked': schools_tracked,
    },
        context_instance=RequestContext(request))

def state_detail(request, stimstate):
    st = get_object_or_404(StateEducationDepartment, state_name_slug=stimstate)
    districts = District.objects.filter(state_education_department=st)
    posts = Post.published_objects.filter(states_in_post=st).order_by('-publication_date')
    links = Link.published_objects.filter(states_tagged=st).order_by('-submitted')
    stim_projects = PrimaryAward.objects.filter(state_funded=st).order_by('-award_date')
    stim_sum = stim_projects.aggregate(Sum('amount_awarded'), Count('amount_awarded'))
    spent_sum = stim_projects.aggregate(Sum('amount_disbursed'))
    try:
        pct_spent = float((spent_sum['amount_disbursed__sum']/ stim_sum['amount_awarded__sum'])*100)
    except TypeError:
        pct_spent = 0
    reports = st.contributions.all()
    journalists = reports.filter(contributor__contributor__contributor_type = "Journalist", contributor__contributor__verified=True)
    citizens = reports.exclude(contributor__contributor__verified = True)
    if request.method == 'POST': # If the form has been submitted...
        form = ContributionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            headline = form.cleaned_data['headline']
            body = form.cleaned_data['body']
            contenttype = ContentType.objects.get_for_model(StateEducationDepartment)
            contribution = Contribution(contributor=request.user, headline=headline, body=body, active=False, content_type=contenttype, object_id=st.id, content_object=st)
            contribution.save()
            return HttpResponseRedirect(st.get_absolute_url())
    else:
        form = ContributionForm() # An unbound form
    return render_to_response('schools/state_detail.html', {
        'state': st,
        'districts': districts,
        'posts': posts,
        'links': links,
        'stim_projects': stim_projects,
        'stim_sum': stim_sum,
        'spent_sum': spent_sum,
        'pct_spent': pct_spent,
        'form': form,
        },
        context_instance=RequestContext(request))
    
def district_detail(request, stimdistrict, stimstate, did):
    st = get_object_or_404(StateEducationDepartment, state_name_slug=stimstate)
    district = get_object_or_404(District, state_education_department=st, id=did)
    demographics = DistrictDemographics.objects.filter(district=district).order_by('-school_year')[:1]
    if demographics[0].total_students > 80000:
        amount = demographics[0].total_students*.25
        high = demographics[0].total_students+amount
        low = demographics[0].total_students-amount
        simdist = DistrictDemographics.objects.filter(total_students__range=(low, high)).exclude(district=district)
        count = simdist.count()
        if count > 25:
            random = True
        else:
            random = False
        compare = simdist.order_by('?')[:25]
    elif demographics[0].total_students > 0:
        amount = demographics[0].total_students*.05
        high = demographics[0].total_students+amount
        low = demographics[0].total_students-amount
        simdist = DistrictDemographics.objects.filter(total_students__range=(low, high)).exclude(district=district)
        count = simdist.count()
        if count > 25:
            random = True
        else:
            random = False
        compare = simdist.order_by('?')[:25]
    else:
        count = 0
        compare = []
        random = False
    posts = Post.published_objects.filter(districts_in_post=district)
    links = Link.published_objects.filter(districts_tagged=district)
    stim_projects = SecondaryAward.objects.filter(district_funded=district)
    stim_sum = stim_projects.aggregate(Sum('amount_awarded'))
    spent_sum = stim_projects.aggregate(Sum('amount_disbursed'))
    try:
        pct_spent = float((spent_sum['amount_disbursed__sum']/ stim_sum['amount_awarded__sum'])*100)
    except:
        pct_spent = 0
    reports = district.contributions.all()
    journalists = reports.filter(contributor__contributor__contributor_type = "Journalist", contributor__contributor__verified=True)
    citizens = reports.exclude(contributor__contributor__verified = True)
    if request.method == 'POST': # If the form has been submitted...
        form = ContributionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            headline = form.cleaned_data['headline']
            body = form.cleaned_data['body']
            contenttype = ContentType.objects.get_for_model(District)
            contribution = Contribution(contributor=request.user, headline=headline, body=body, active=False, content_type=contenttype, object_id=district.id, content_object=district)
            contribution.save()
            return HttpResponseRedirect(district.get_absolute_url())
    else:
        form = ContributionForm() # An unbound form
    return render_to_response('schools/district_detail.html', {
        'state': st,
        'district': district,
        'demographics': demographics,
        'compare': compare,
        'posts': posts,
        'links': links,
        'stim_projects': stim_projects,
        'stim_sum': stim_sum,
        'spent_sum': spent_sum,
        'pct_spent': pct_spent,
        'form': form,
        'journalists': journalists,
        'citizens': citizens,
        'random': random,
        'count': count,
    },
        context_instance=RequestContext(request))
    
def school_detail(request, stimdistrict, stimstate, stimschool):
    st = get_object_or_404(StateEducationDepartment, state_name_slug=stimstate)
    district = get_object_or_404(District, state_education_department=st, district_name_slug=stimdistrict)
    school = get_object_or_404(School, district=district, school_name_slug=stimschool)
    demographics = get_list_or_404(SchoolDemographics, school=school)
    posts = Post.published_objects.filter(schools_in_post=school)
    links = Link.published_objects.filter(schools_tagged=school)
    stim_projects = PrimaryAward.objects.filter(school_funded=school)
    stim_sum = stim_projects.aggregate(Sum('amount_awarded'))
    if request.method == 'POST': # If the form has been submitted...
        form = ContributionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            headline = form.cleaned_data['headline']
            body = form.cleaned_data['body']
            contenttype = ContentType.objects.get_for_model(School)
            contribution = Contribution(contributor=request.user, headline=headline, body=body, active=False, content_type=contenttype, object_id=school.id, content_object=school)
            contribution.save()
            return HttpResponseRedirect(district.get_absolute_url())
    else:
        form = ContributionForm() # An unbound form
    return render_to_response('schools/school_detail.html', {
        'state': st,
        'district': district,
        'school': school,
        'demographics': demographics,
        'posts': posts,
        'links': links,
        'stim_projects': stim_projects,
        'stim_sum': stim_sum,
        'form': form,
    },
        context_instance=RequestContext(request))

def state_csv(request, stimstate):
    st = get_object_or_404(StateEducationDepartment, state_name_slug=stimstate)
    primary = PrimaryAward.objects.filter(state_funded=st)
    secondary = SecondaryAward.objects.filter(recipient_state=st.state.state_abbreviation)
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%sgrants.csv' % stimstate
    t = loader.get_template('grants.csv')
    c = Context({
        'primary': primary,
        'secondary': secondary,
    })
    response.write(t.render(c))
    return response

