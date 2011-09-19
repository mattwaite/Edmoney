from django.db import models
from django.forms import ModelForm

class ContactList(models.Model):
    email = models.EmailField()
    def __unicode__(self):
        return self.email
    
class ContactListForm(ModelForm):
    class Meta:
        model = ContactList

