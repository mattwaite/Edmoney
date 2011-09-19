from django.shortcuts import render_to_response, get_object_or_404
from stimulustracker.staff.models import Staffer
from stimulustracker.blog.models import Post

def main(request):
    staffers = Staffer.objects.order_by('last_name').select_related()
    recent_posts = Post.published_objects.order_by('-publication_date').select_related()[:5]
    return render_to_response('staff/staff_main.html', {
        'staffers': staffers,
        'recent_posts': recent_posts,
    })
    
def detail(request, slug):
    staffer = get_object_or_404(Staffer, name_slug=slug)
    recent_author_posts = Post.published_objects.filter(author=staffer).order_by('-publication_date').select_related()[:10]
    recent_posts = Post.published_objects.order_by('-publication_date').select_related()[:5]
    return render_to_response('staff/staff_detail.html', {
        'staffer': staffer,
        'recent_posts': recent_posts,
        'recent_author_posts': recent_author_posts,
    })