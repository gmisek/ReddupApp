from django.conf.urls import patterns, include, url
from scru import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reddup.views.home', name='home'),
    # url(r'^reddup/', include('reddup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'scru.views.index', name='index'),
    url(r'^issue/open', 'scru.views.open_issue', name='open_issue'),
    url(r'^issue/(?P<issue_id>\d+)/close', 'scru.views.close_issue', name='close_issue'),
    url(r'^issue/(?P<issue_id>\d+)/reup', 'scru.views.reup_issue', name='reup_issue'),
    url(r'^pledge/new', 'scru.views.create_pledge', name='create_pledge'),
   # url(r'/^$',)
)
