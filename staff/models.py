from django.db import models

class Staffer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    name_slug = models.SlugField(help_text="Don't change this unless you know what you're doing.")
    photo = models.ImageField(blank=True, null=True, upload_to="/staff/", help_text="Dimensions for the photo are 76 px x 76 px")
    email_address = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    def get_absolute_url(self):
        return "/staff/%s/" % self.name_slug
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)