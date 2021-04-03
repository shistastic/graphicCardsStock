from django.contrib import admin
from django.urls import path

from checkstock import views

urlpatterns = [
    path('', views.checkHTML, name='checkHTML'),

]
