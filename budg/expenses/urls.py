
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('base/', views.base, name="base"),
    path('add_expense/', views.add_expense, name="add_expense"),
]
