#!/usr/bin/python
#coding: utf-8
from django.conf.urls.defaults import patterns, include, url
from mysite.view import hello,login,search_form,test_form,search
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^test/$',test_form),
    url(r'^index/(\d{1,2})$',login),
    url(r'^search-form/$',search_form),
    url(r'^search/$',search),
  
)
