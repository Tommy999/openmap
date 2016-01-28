from django.conf.urls import *
from django.contrib import admin
from views import *



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^index/$',
        index),

    url(r'^test/$',
        map_test),

    url(r'^test2/$',
        map_test2),
    url(r'^angular/$',
        angular),
)