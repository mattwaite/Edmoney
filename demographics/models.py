from django.db import models
from stimulustracker.schools.models import School, District

class SchoolDemographics(models.Model):
    school = models.ForeignKey(School)
    school_year = models.CharField(max_length=150)
    title_i = models.BooleanField()
    all_school_title_i = models.BooleanField()
    magnet_school = models.BooleanField()
    charter_school = models.BooleanField()
    frl_students = models.IntegerField(blank=True, null=True)
    migrant_students = models.IntegerField(blank=True, null=True)
    american_indian_students = models.IntegerField(blank=True, null=True)
    asian_pacific_islander_students = models.IntegerField(blank=True, null=True)
    hispanic_students = models.IntegerField(blank=True, null=True)
    black_students = models.IntegerField(blank=True, null=True)
    white_students = models.IntegerField(blank=True, null=True)
    total_students = models.IntegerField()
    total_teachers = models.FloatField()
    student_teacher_ratio = models.FloatField()
    class Meta:
        verbose_name_plural = "school demographic reports"
    def __unicode__(self):
        return "%s: %s" % (self.school, self.school_year)
    
class DistrictDemographics(models.Model):
    district = models.ForeignKey(District)
    school_year = models.CharField(max_length=150)
    total_schools = models.IntegerField()
    total_students = models.IntegerField()
    total_teachers = models.FloatField()
    class Meta:
        verbose_name_plural = "district demographic reports"
    def clean_total_students(self):
        if self.total_students < 0:
            return "Not Reported"
        else:
            return self.total_students
    def __unicode__(self):
        return "%s: %s" % (self.district, self.school_year)
        