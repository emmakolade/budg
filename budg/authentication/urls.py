
from django.contrib import admin
from django.urls import path
from .views import Registration, UsernameValidation, Login, Logout
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [

    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('register/', Registration.as_view(), name="register"),
    path('username_validate/', csrf_exempt(UsernameValidation.as_view()),
         name="username_validate"),
    # path('email_validate/', csrf_exempt(EmailValidation.as_view()), name="email_validate"),

    
    path("password_reset", views.password_reset_request, name="password_reset")

    # path('password_reset/', PasswordResetRequest.as_view(), name="password_reset"),
    # path("password_reset", views.password_reset_request, name="password_reset")

]
