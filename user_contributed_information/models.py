from django.db import models
from django.contrib.comments.models import Comment
from django.contrib.auth.models import User, UserManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.forms import ModelForm

CONTRIBUTOR_TYPE = (
    ('Parent', 'Parent'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
    ('Citizen', 'Citizen'),
    ('Journalist', 'Journalist'),
    ('Other', 'Other'),
)

class Contributor(models.Model):
    user = models.ForeignKey(User, unique=True)
    contributor_type = models.CharField(max_length=150, choices=CONTRIBUTOR_TYPE)
    name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    journalist_employer = models.CharField(max_length=255, blank=True, null=True)
    journalist_employer_url = models.URLField(verify_exists=True, blank=True, null=True)
    verified = models.BooleanField()
    objects = UserManager()
    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
    def __unicode__(self):
        return self.user.username

class Contribution(models.Model):
    contributor = models.ForeignKey(User)
    headline = models.CharField(max_length=255)
    body = models.TextField()
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    def get_absolute_url(self):
        return "/contributions/%s/" % self.id
    def __unicode__(self):
        return self.headline

class ContributionForm(ModelForm):
    class Meta:
        model = Contribution
        fields = ('headline', 'body')