from django.contrib import admin
from .models import *

admin.site.register(Issue)
admin.site.register(IssueUser)
admin.site.register(Pledge)
admin.site.register(LocationType)
admin.site.register(Category)