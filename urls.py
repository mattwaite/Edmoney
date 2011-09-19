from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()
from django.contrib.sitemaps import GenericSitemap

from stimulustracker.blog.models import Post
from stimulustracker.home.feeds import LatestEntries

from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect

from registration.views import activate
from registration.views import register

blog_dict = {
    'queryset': Post.published_objects.order_by('-publication_date').select_related(),
    'date_field': 'publication_date',
    'extra_context' : {'recent_posts' : Post.published_objects.order_by('-publication_date').select_related()[:5]},
    'allow_future' : True,
}

feeds = {
    'blog': LatestEntries,
}

sitemaps = {
    'blog': GenericSitemap(blog_dict, priority=0.6),
}

urlpatterns = patterns('django.views.generic.simple',
#    (r'^$',             'direct_to_template', {'template': 'homepage.html'}),
    (r'^links/thanks/$',             'direct_to_template', {'template': 'links/thanks.html'}),
    (r'^contribute/thanks/$',             'direct_to_template', {'template': 'contribute/thanks.html'}),
    (r'^thanks/$',             'direct_to_template', {'template': 'thanks.html'}),
    (r'^contact/thanks/$',             'direct_to_template', {'template': 'contact/contact_thanks.html'}),
)

urlpatterns += patterns('django.views.generic.date_based',
    (r'^blog/$', 'archive_index', dict(blog_dict, template_name='blog/blog_main.html')),
    (r'^blog/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', dict(blog_dict, template_name='blog/blog_archive_month.html')),
    (r'^blog/(?P<year>\d{4})/$', 'archive_year',  dict(blog_dict, template_name='blog/blog_archive_year.html')),   
    (r'^blog/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(blog_dict, slug_field='title_slug', template_name='blog/blog_detail.html')),
)

urlpatterns += patterns('',
    (r'^$', 'stimulustracker.home.views.homepage'),
    (r'^contact/$', 'stimulustracker.home.views.contact'),
    (r'^links/$', 'stimulustracker.links.views.main'),
    (r'^staff/$', 'stimulustracker.staff.views.main'),
    (r'^staff/(?P<slug>[-\w]+)/$', 'stimulustracker.staff.views.detail'),
    (r'^contribute/links/$', 'stimulustracker.links.views.contribute'),
    (r'^data/schools/$', 'stimulustracker.schools.views.schools_main'),
    (r'^data/schools/(?P<stimstate>[-\w]+)/$', 'stimulustracker.schools.views.state_detail'),
    (r'^data/schools/(?P<stimstate>[-\w]+)/csv/$', 'stimulustracker.schools.views.state_csv'),
    (r'^data/schools/(?P<stimstate>[-\w]+)/(?P<stimdistrict>[-\w]+)/(?P<did>\d+)/$', 'stimulustracker.schools.views.district_detail'),
    (r'^data/schools/(?P<stimstate>[-\w]+)/(?P<stimdistrict>[-\w]+)/(?P<stimschool>[-\w]+)/$', 'stimulustracker.schools.views.school_detail'),
    (r'^contributions/(?P<contribid>\d+)/', 'stimulustracker.user_contributed_information.views.contribution_detail'),
    (r'^stimulus/primary-awards/(?P<primarystimid>[-\w]+)/$', 'stimulustracker.stimulus.views.primary_detail'),
    (r'^stimulus/secondary-awards/(?P<secondarystimid>[-\w]+)/$', 'stimulustracker.stimulus.views.secondary_detail'),
    (r'^special-reports/(?P<special>[-\w]+)/$', 'stimulustracker.specials.views.specials_detail'),
    (r'^search/', include('haystack.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^profiles/', include('profiles.urls')),
    (r'^accounts/', include('stimulustracker.registration.backends.default.urls')),
#    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root': '/opt/django-projects/stimulustracker/designs/'}),
)
