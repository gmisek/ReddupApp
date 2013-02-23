from django.db import models
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
    status = models.CharField(max_length = 100)
    description = models.CharField(max_length=500)
    before_img = models.ImageField(upload_to = "static/before_img/", null=True)
    after_img = models.ImageField(upload_to = "static/after_img/", null=True)
    date_opened = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_closed = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    opener_id = models.ForeignKey(User, related_name='issue_opener')
    closer_id = models.ForeignKey(User, related_name='issue_closer')
    cleaner_id = models.ForeignKey(User, related_name='issue_cleaner')
    category_id = models.ForeignKey(Category)
    reported_to_311 = models.NullBooleanField()
    geom = PointField()
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
    radius = models.PositiveIntegerField(default=1, blank=True, null=True)