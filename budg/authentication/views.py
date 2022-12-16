from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.validators import validate_email

from django.core.mail import EmailMessage


class Registration(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        # get user data from the form
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {
            # to pre-populate the form fields with the previous input incase of an error
            'fieldvalues': request.POST
        }

        # check if the username or email already exists in the database.
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 8:
                    messages.error(request, 'password is too short')
                    return render(request, 'authentication/register.html', context)

                # create a new user with the specified username, email, and password.
                user = User.objects.create_user(
                    username=username, email=email)
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(
                    request, 'account created sucessfully for ' + username)
                return redirect('login')

        return render(request, 'authentication/register.html')


class UsernameValidation(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not username.isalnum():
            return JsonResponse({'username_error': 'username should only contain letters and numbers'}, status=400)
        # if usrname exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username already exsits.. try another one'}, status=409)


class Login(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try to authenticate the user with the given credentials
        if username and password:
            user = authenticate(username=username, password=password)

            # If the user is authenticated and active, log them in and redirect them to the home page
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome, ' +
                                 username + ' you are now logged in')
                return redirect('home')

            messages.error(request, 'Invalid credentials, try again')

        # If the user has not provided all the required fields, display an error message
        else:
            messages.error(request, 'Please fill all fields')

        return render(request, 'authentication/login.html')


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you have been logged out')
        return redirect('base')
