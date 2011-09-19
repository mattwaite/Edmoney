from django.contrib.gis.db import models
from django.template.defaultfilters import slugify, urlize

class State(models.Model):
    state_name = models.CharField(max_length=50)
    state_slug = models.SlugField()
    state_fips = models.CharField(max_length=3, db_index=True)
    state_abbreviation = models.CharField(max_length=2, blank=True, null=True)
    other_state_id = models.CharField(max_length=15, blank=True, null=True)
    poly = models.MultiPolygonField()
    objects = models.GeoManager()
    class Meta:
        ordering = ['state_name']
    def save(self, force_insert=False, force_update=False):
        self.state_slug = slugify(self.state_name)
        super(State, self).save(force_insert, force_update)
    def __unicode__(self):
        return self.state_name
        
class County(models.Model):
    state = models.ForeignKey(State, null=True)
    state_fips = models.CharField(max_length=6, db_index=True)
    county_name = models.CharField(max_length=255)
    county_slug = models.SlugField()
    county_fips = models.CharField(max_length=6, db_index=True)
    other_county_id = models.CharField(max_length=15, blank=True, null=True)
    poly = models.MultiPolygonField()
    objects = models.GeoManager()
    class Meta:
        verbose_name_plural = 'counties'
        ordering = ['county_name']
    def save(self, force_insert=False, force_update=False):
        self.county_slug = slugify(self.county_name)
        super(County, self).save(force_insert, force_update)
    def __unicode__(self):
        return "%s County, %s" % (self.county_name, self.state)
        
class City(models.Model):
    state = models.ForeignKey(State)
    city_name = models.CharField(max_length=255)
    city_slug = models.SlugField()
    city_fips = models.CharField(max_length=10, db_index=True, blank=True, null=True)
    other_city_id = models.CharField(max_length=15, blank=True, null=True)
    poly = models.MultiPolygonField()
    point = models.PointField()
    objects = models.GeoManager()
    class Meta:
        verbose_name_plural = 'cities'
    def __unicode__(self):
        return "%s, %s" % (self.city_name, self.state.state_name)
        
class Zipcode(models.Model):
    zipcode = models.CharField(max_length=5)
    poly = models.MultiPolygonField()
    objects = models.GeoManager()
    def __unicode__(self):
        return self.zipcode
        
class CongressionalDistrict(models.Model):
    state = models.ForeignKey(State, null=True)
    state_fips = models.CharField(max_length=50)
    congressional_district_number = models.CharField(max_length=5)
    congressional_district = models.CharField(max_length=50)    
    congressional_district_slug= models.SlugField()
    poly = models.MultiPolygonField()
    objects = models.GeoManager()
    def save(self, force_insert=False, force_update=False):
        self.congressional_district = "Congressional District %s" % self.congressional_district_number
        self.congressional_district_slug = slugify(self.congressional_district)
        super(CongressionalDistrict, self).save(force_insert, force_update)    
    def __unicode__(self):
        return "%s in %s" % (self.congressional_district, self.state)