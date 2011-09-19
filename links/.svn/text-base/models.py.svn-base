from django.db import models
from django.forms import ModelForm
from stimulustracker.schools.models import StateEducationDepartment, District, School
import datetime

class PublishedObjectsManager(models.Manager):
    def get_query_set(self):
        rightnow = datetime.datetime.today()
        return super(PublishedObjectsManager, self).get_query_set().filter(active=True, submitted__lte=rightnow)

class Link(models.Model):
    link_title = models.CharField(max_length=255)
    link_url = models.URLField(verify_exists=True)
    link_description = models.TextField(help_text="Summarize what's at the link here. Keep it short.")
    submitted = models.DateTimeField(auto_now_add=True)
    states_tagged = models.ManyToManyField(StateEducationDepartment, blank=True, null=True)
    districts_tagged = models.ManyToManyField(District, blank=True, null=True)
    schools_tagged = models.ManyToManyField(School, blank=True, null=True)
    active = models.BooleanField(default=False)
    objects = models.Manager()
    published_objects = PublishedObjectsManager()
    def __unicode__(self):
        return self.link_title
    
class LinkForm(ModelForm):
    class Meta:
        model = Link
        exclude = ('states_tagged','districts_tagged', 'schools_tagged','active')
