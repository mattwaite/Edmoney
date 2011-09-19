from stimulustracker.blog.models import Post
from stimulustracker.links.models import Link
from stimulustracker.home.models import ContactListForm
from stimulustracker.specials.models import SpecialReport
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_list

from profiles import utils


def homepage(request):
    latest_posts = Post.published_objects.order_by('-publication_date')[:5]
    latest_links = Link.published_objects.order_by('-submitted')[:5]
    try:
        welcome = Post.published_objects.get(id=6)
    except:
        welcome = ""
    special_report = SpecialReport.objects.exclude(active=False)[:1]
    return render_to_response('new_home_homepage.html', {
        'latest_posts': latest_posts,
        'latest_links': latest_links,
        'welcome': welcome,
        'special_report': special_report,
    })


def oldhomepage(request):
    if request.method == 'POST':
        form = ContactListForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            f = form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactListForm(initial={'email': 'youraddress@example.com'})
    latest_posts = Post.published_objects.order_by('-publication_date')[:5]
    latest_links = Link.published_objects.order_by('-submitted')[:5]
    try:
        welcome = Post.published_objects.get(id=6)
    except:
        welcome = ""
    return render_to_response('home_homepage.html', {
        'latest_posts': latest_posts,
        'latest_links': latest_links,
        'form': form,
        'welcome': welcome,
    })

def registration_complete(request, form_class=None, success_url=None,
                   template_name='registration/registration_complete.html',
                   extra_context=None):
    """
    Create a profile for the current user, if one doesn't already
    exist.
    
    If the user already has a profile, as determined by
    ``request.user.get_profile()``, a redirect will be issued to the
    :view:`profiles.views.edit_profile` view. If no profile model has
    been specified in the ``AUTH_PROFILE_MODULE`` setting,
    ``django.contrib.auth.models.SiteProfileNotAvailable`` will be
    raised.
    
    **Optional arguments:**
    
    ``extra_context``
        A dictionary of variables to add to the template context. Any
        callable object in this dictionary will be called to produce
        the end result which appears in the context.

    ``form_class``
        The form class to use for validating and creating the user
        profile. This form class must define a method named
        ``save()``, implementing the same argument signature as the
        ``save()`` method of a standard Django ``ModelForm`` (this
        view will call ``save(commit=False)`` to obtain the profile
        object, and fill in the user before the final save). If the
        profile object includes many-to-many relations, the convention
        established by ``ModelForm`` of using a method named
        ``save_m2m()`` will be used, and so your form class should
        also define this method.
        
        If this argument is not supplied, this view will use a
        ``ModelForm`` automatically generated from the model specified
        by ``AUTH_PROFILE_MODULE``.
    
    ``success_url``
        The URL to redirect to after successful profile creation. If
        this argument is not supplied, this will default to the URL of
        :view:`profiles.views.profile_detail` for the newly-created
        profile object.
    
    ``template_name``
        The template to use when displaying the profile-creation
        form. If not supplied, this will default to
        :template:`profiles/create_profile.html`.
    
    **Context:**
    
    ``form``
        The profile-creation form.
    
    **Template:**
    
    ``template_name`` keyword argument, or
    :template:`profiles/create_profile.html`.
    
    """
    try:
        profile_obj = request.user.get_profile()
        return HttpResponseRedirect(reverse('profiles_edit_profile'))
    except ObjectDoesNotExist:
        pass
    
    #
    # We set up success_url here, rather than as the default value for
    # the argument. Trying to do it as the argument's default would
    # mean evaluating the call to reverse() at the time this module is
    # first imported, which introduces a circular dependency: to
    # perform the reverse lookup we need access to profiles/urls.py,
    # but profiles/urls.py in turn imports this module.
    #
    
    if success_url is None:
        success_url = reverse('profiles_profile_detail',
                              kwargs={ 'username': request.user.username })
    if form_class is None:
        form_class = utils.get_profile_form()
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            profile_obj = form.save(commit=False)
            profile_obj.user = request.user
            profile_obj.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            return HttpResponseRedirect(success_url)
    else:
        form = form_class()
    
    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value
    
    return render_to_response(template_name,
                              { 'form': form },
                              context_instance=context)
create_profile = login_required(registration_complete)

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.core.mail import send_mail

def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             if request.POST['email'] == "":
#                 email = "Not Provided"
#             else:
#                 email = request.POST['email']
#             send_mail(
#                 'Contact from %s RE: %s' % (email, request.POST['subject']),
#                 request.POST['message'],
#                 request.POST.get('email',),
#                 ['matt.waite@gmail.com', 'lcrouch@ewa.org'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact/contact_form.html', {
#         'errors': errors,
#         'subject': request.POST.get('subject', ''),
#         'message': request.POST.get('message', ''),
#         'email': request.POST.get('email', ''),
    })