# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

from django.urls import path
from . import views
app_name ='search'
urlpatterns = [
    path('', views.index, name='index'),
]
