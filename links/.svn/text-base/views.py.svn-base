from stimulustracker.links.models import Link
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect
from stimulustracker.links.models import LinkForm
from django.views.decorators.cache import cache_page

def main(request):
    link_list = Link.published_objects.order_by('-submitted')
    paginator = Paginator(link_list, 25) # Show 25 contacts per page
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        links = paginator.page(page)
    except (EmptyPage, InvalidPage):
        links = paginator.page(paginator.num_pages)
    return render_to_response ('links/main.html', {
        'links': links,
    })
main = cache_page(main, 60 * 10)

def contribute(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LinkForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            cd = form.cleaned_data
            f = form.save()
            from django.core.mail import send_mail
            subject = "A new story was contributed and needs reviewing"
            message = "A new story was just submitted."
            sender = "hottype1234@gmail.com"
            recipients = ['matt.waite@gmail.com', 'lcrouch@ewa.org', 'torres.mcnelly@gmail.com']
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/contribute/thanks/')
    else:
        form = LinkForm() # An unbound form
    return render_to_response('contribute/contribute_links.html', {
        'form': form,
    })
