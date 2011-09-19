from django.db import models
from stimulustracker.blog.models import Post
from stimulustracker.links.models import Link

class SpecialReport(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    chatter = models.TextField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, upload_to="specials-logos/", help_text="The logo is 80 px by 80 px")
    mainbars = models.ManyToManyField(Post, related_name="mainbar_set")
    sidebars = models.ManyToManyField(Post, blank=True, null=True, related_name="sidebar_set")
    links = models.ManyToManyField(Link)
    active = models.BooleanField()
    def get_absolute_url(self):
        return "/special-reports/%s/" % self.name_slug
    def __unicode__(self):
        return self.name