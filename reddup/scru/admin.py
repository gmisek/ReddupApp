#from django.contrib import admin
from .models import *
from django.contrib.gis import admin

admin.site.register(Issue, admin.OSMGeoAdmin)
admin.site.register(Pledge, admin.OSMGeoAdmin)

admin.site.register(IssueUser)

admin.site.register(LocationType)
admin.site.register(Category)