from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,include
from . import views

urlpatterns = [
    path('flightList/', views.flightList,name='flightList'),
    path('flightList/<int:pk>/', views.flightList_details,name='flightList_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)