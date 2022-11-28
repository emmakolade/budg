
from django.contrib import admin
from django.urls import path
from .views import Registration, Login

urlpatterns = [
    
    path('login/', Login.as_view(), name="login"),
    path('register/', Registration.as_view(), name="register"),
]
