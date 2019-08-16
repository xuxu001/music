# -*- coding:utf-8 -*-

from django.urls import path
from . import views
app_name ='play'
urlpatterns = [
    path('', views.index),
]
