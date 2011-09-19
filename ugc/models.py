from django.db import models
from django.contrib.auth.models import User, UserManager
from stimulustracker.schools.models import School

CONTRIBUTOR_TYPE = (
    ('Parent', 'Parent'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
    ('Citizen', 'Citizen'),
    ('Journalist', 'Journalist')
)

class Contributor(User):
    contributor_type = models.CharField(max_length=150, choices=CONTRIBUTOR_TYPE)
    bio = models.TextField()
    objects = UserManager()
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
class Contribution(models.Model):
    contributor = models.ForeignKey(Contributor)
    school = models.ForeignKey(School)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField()
    class Meta:
        ordering = ['comment_date']
    def __unicode__(self):
        return "%s on %s" % (self.contributor, self.school)