from django.contrib.gis.db import models
from stimulustracker.geography.models import State, City, Zipcode, County
from stimulustracker.user_contributed_information.models import Contribution
from django.contrib.contenttypes import generic

class SchoolType(models.Model):
    school_type = models.CharField(max_length=50)
    school_type_slug = models.SlugField()
    def __unicode__(self):
        return self.school_type

class SchoolStatus(models.Model):
    school_status = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'school statuses'
    def __unicode__(self):
        return self.school_status

class DistrictType(models.Model):
    district_type_short = models.CharField(max_length=255)
    district_type = models.TextField()
    def __unicode__(self):
        return self.district_type_short

class DistrictStatus(models.Model):
    district_status = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'district statuses'
    def __unicode__(self):
        return self.district_status

class StateEducationDepartment(models.Model):
    state = models.ForeignKey(State)
    state_name = models.CharField(max_length=255)
    state_name_slug = models.SlugField()
    total_students = models.IntegerField(blank=True, null=True)
    total_teachers = models.FloatField(blank=True, null=True)
    total_budget = models.FloatField(blank=True, null=True)
    contributions = generic.GenericRelation(Contribution)
    class Meta:
        ordering = ['state_name']
    def get_absolute_url(self):
        return "/data/schools/%s/" % self.state_name_slug
    def __unicode__(self):
        return self.state_name

class District(models.Model):
    state_education_department = models.ForeignKey(StateEducationDepartment)
    county = models.ForeignKey(County, blank=True, null=True)
    district_id = models.CharField(max_length=7, db_index=True)
    district_name = models.CharField(max_length=150)
    district_name_slug = models.SlugField()    
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=255)
    point = models.PointField()
    district_type = models.ForeignKey(DistrictType)
    district_status = models.ForeignKey(DistrictStatus)
    contributions = generic.GenericRelation(Contribution)
    objects = models.GeoManager()
    class Meta:
        ordering = ['district_name']
    def get_absolute_url(self):
        return "/data/schools/%s/%s/%s/" % (self.state_education_department.state_name_slug, self.district_name_slug, self.id)
    def __unicode__(self):
        return self.district_name

class School(models.Model):
    district = models.ForeignKey(District)
    ccd_school_id = models.CharField(max_length=12, db_index=True)    
    school_name = models.CharField(max_length=255)
    school_name_slug = models.SlugField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=255)
    school_type = models.ForeignKey(SchoolType)
    school_status = models.ForeignKey(SchoolStatus)
    point = models.PointField()
    contributions = generic.GenericRelation(Contribution)
    objects = models.GeoManager()
    class Meta:
        ordering = ['school_name']
    def get_absolute_url(self):
        return "/data/schools/%s/%s/%s" % (self.district.state_education_department.state_name_slug, self.district.district_name_slug, self.school_name_slug)
    def __unicode__(self):
        return self.school_name
