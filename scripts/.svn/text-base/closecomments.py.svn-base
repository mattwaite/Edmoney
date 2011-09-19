from django.core.management import setup_environ
import sys, random, string, csv
sys.path.append('/opt/django-projects/')
from stimulustracker import settings
setup_environ(settings)

from stimulustracker.blog.models import Post
import datetime
from datetime import timedelta

t = timedelta(60)
td = datetime.datetime.today()
cutoff = td-t

p = Post.objects.filter(publication_date__lte=cutoff)

for object in p:
    object.enable_comments = False
    object.save()