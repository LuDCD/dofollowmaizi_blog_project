#!/usr/bin/python
# -*- coding:utf8 -*-

from django.conf.urls import include, url

from blog.views import index

urlpatterns = [
    url(r'^$', index, name='index'),

]