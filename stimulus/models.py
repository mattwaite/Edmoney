from django.db import models
from stimulustracker.schools.models import StateEducationDepartment, District, School

class Agency(models.Model):
    agency_name = models.CharField(max_length=255)
    agency_name_slug = models.SlugField()
    class Meta:
        verbose_name_plural = "Agencies"
    def __unicode__(self):
        return self.agency_name

class AwardType(models.Model):
    award_type = models.CharField(max_length=150)
    award_type_slug = models.SlugField()
    def __unicode__(self):
        return self.award_type

class PrimaryAward(models.Model):
    arra_id = models.IntegerField(db_index=True)
    award_type = models.ForeignKey(AwardType)
    awarding_agency = models.ForeignKey(Agency)
    award_date = models.DateField()
    recipient_name = models.CharField(max_length=255)
    recipient_state = models.CharField(max_length=100, blank=True, null=True)
    recipient_zipcode = models.CharField(max_length=10, blank=True, null=True)
    state_funded = models.ForeignKey(StateEducationDepartment, blank=True, null=True)
    district_funded = models.ForeignKey(District, blank=True, null=True)
    school_funded = models.ForeignKey(School, blank=True, null=True)
    award_id = models.CharField(max_length=255, db_index=True)
    award_description = models.TextField(blank=True, null=True)
    amount_awarded = models.FloatField(blank=True, null=True)
    amount_disbursed = models.FloatField(blank=True, null=True)
    reported_number_of_jobs_created = models.FloatField(blank=True, null=True)
    jobs_created_description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField()
    clean_short_name = models.CharField(max_length=255, blank=True, null=True)
    clean_award_description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name_plural = "Primary stimulus awards"
    def get_absolute_url(self):
        return "/stimulus/primary-awards/%s/" % self.arra_id
    def __unicode__(self):
        return self.recipient_name

class SecondaryManager(models.Manager):
    def get_query_set(self):
        return super(SecondaryManager, self).get_query_set().filter(district_funded=None).exclude(recipient_name__icontains="charter")

class SecondaryAward(models.Model):
    primary_award = models.ForeignKey(PrimaryAward)
    award_key = models.IntegerField()
    award_type = models.ForeignKey(AwardType)
    awarding_agency = models.ForeignKey(Agency)
    award_date = models.DateField()
    recipient_name = models.CharField(max_length=255)
    recipient_state = models.CharField(max_length=100, blank=True, null=True)
    recipient_zipcode = models.CharField(max_length=10, blank=True, null=True)
    recipient_sub_duns_number = models.CharField(max_length=150)
    state_funded = models.ForeignKey(StateEducationDepartment, blank=True, null=True)
    district_funded = models.ForeignKey(District, blank=True, null=True)
    school_funded = models.ForeignKey(School, blank=True, null=True)
    award_id = models.CharField(max_length=255, db_index=True)
    award_description = models.TextField(blank=True, null=True)
    amount_awarded = models.FloatField(blank=True, null=True)
    amount_disbursed = models.FloatField(blank=True, null=True)
    reported_number_of_jobs_created = models.FloatField(blank=True, null=True)
    jobs_created_description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField()
#    objects = SecondaryManager()
    class Meta:
        verbose_name_plural = "Secondary stimulus awards"
    def get_absolute_url(self):
        return "/stimulus/secondary-awards/%s/" % self.id
    def __unicode__(self):
        return self.recipient_name