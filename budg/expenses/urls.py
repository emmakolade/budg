
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.login, name="login"),
    # path('register/', views.register, name="register"),
    path('add_expense', views.add_expense, name="add_expense"),
]
