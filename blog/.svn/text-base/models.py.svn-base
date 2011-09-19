from django.db import models
from stimulustracker.schools.models import District, School, StateEducationDepartment
from stimulustracker.staff.models import Staffer
import datetime

class PublishedObjectsManager(models.Manager):
    def get_query_set(self):
        return super(PublishedObjectsManager, self).get_query_set().filter(active=True)

class Post(models.Model):
    author = models.ForeignKey(Staffer)
    title = models.CharField(max_length=255)
    title_slug = models.SlugField(unique=True, max_length=255, help_text="Don't change this unless you know what you're doing.")
    body = models.TextField()
    active = models.BooleanField(default=False, help_text="Check this and it's live to the world.")
    enable_comments = models.BooleanField(default=True, help_text="Use this to turn comments on or off on a specific post. It defaults to on.")
    updated_date = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField()
    schools_in_post = models.ManyToManyField(School, blank=True, null=True)
    districts_in_post = models.ManyToManyField(District, blank=True, null=True)
    states_in_post = models.ManyToManyField(StateEducationDepartment, blank=True, null=True)
    objects = models.Manager()
    published_objects = PublishedObjectsManager()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-publication_date']    
    def get_absolute_url(self):
        return "/blog/%s%s/" % (self.publication_date.strftime('%Y/%b/%d/').lower(), self.title_slug)