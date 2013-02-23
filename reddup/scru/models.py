#from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    appkey = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class LocationType(models.Model):
    name = models.CharField(max_length=100)
    appkey = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Issue(models.Model):
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    before_img = models.ImageField(upload_to = "static/before_img/", blank=True, null=True)
    after_img = models.ImageField(upload_to = "static/after_img/", blank=True, null=True)
    date_opened = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_closed = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    opener_id = models.ForeignKey(User, related_name='issue_opener')
    closer_id = models.ForeignKey(User, related_name='issue_closer', blank=True, null=True, default=None)
    cleaner_id = models.ForeignKey(User, related_name='issue_cleaner', blank=True, null=True, default=None)
    category_id = models.ForeignKey(Category)
    reported_to_311 = models.NullBooleanField(default=False)
    geom = PointField()
    objects = models.GeoManager()
    location_type_id = models.ForeignKey(LocationType)
    def __unicode__(self):
        return self.description

class Claim(models.Model):
    issue_id = models.ForeignKey(Issue)
    user_id = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class IssueUser(models.Model):
    issue_id = models.ForeignKey(Issue)
    user_id = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Pledge(models.Model):
    user_id = models.ForeignKey(User)
    geom = PointField()
    objects = models.GeoManager()
    radius = models.PositiveIntegerField(default=1, blank=True, null=True)