import datetime
from haystack.indexes import *
from haystack import site
from stimulustracker.schools.models import District, School, StateEducationDepartment


class StateIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

class DistrictIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

#class SchoolIndex(SearchIndex):
#    text = CharField(document=True, use_template=True)


site.register(District, DistrictIndex)
site.register(StateEducationDepartment, StateIndex)
#site.register(School, SchoolIndex)