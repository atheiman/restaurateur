from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^browse/', include('browse.urls', namespace='browse')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^staff/', include('staff.urls', namespace='staff')),
    url(r'^admin/', include(admin.site.urls)),
)
