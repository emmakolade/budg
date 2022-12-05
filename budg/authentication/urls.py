
from django.contrib import admin
from django.urls import path
from .views import Registration, Login, UsernameValidation, EmailValidation
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('login/', Login.as_view(), name="login"),
    path('register/', Registration.as_view(), name="register"),
    path('username_validate/', csrf_exempt(UsernameValidation.as_view()),
         name="username_validate"),
    path('email_validate/', csrf_exempt(EmailValidation.as_view()),
         name="email_validate"),

]
