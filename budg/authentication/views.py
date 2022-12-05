from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from validate_email import validate_email
from django.contrib import messages, auth

from django.core.mail import EmailMessage
# Create your views here.

# def registrationPage(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form =


class Registration(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        # get user data

        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {
            'fieldvalues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 8:
                    messages.error(request, 'password is too short')
                    return render(request, 'authentication/register.html', context)
                user = User.objects.create_user(
                    username=username, email=email,)
                user.set_password(password)
                user.is_active = False
                user.save()
                # email_subject = 'kindly activate your account'
                # email_body = 'test Budg'
                # email = EmailMessage(
                #     email_subject,
                #     email_body,
                #     'noreply@kolade.com',
                #     [email],
                # )
                # email.send(fail_silently=False)
                messages.success(
                    request, 'account created sucessfully for ' + username)
                return redirect('login')
                # return render(request, 'authentication/register.html')
        return render(request, 'authentication/register.html')


class Login(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username+' you are now logged in')
                    return redirect('home')
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'authentication/login.html')
            messages.error(
                request, 'Invalid credentials,try again')
            return render(request, 'authentication/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'authentication/login.html')


# def loginPage(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'credentials invalid')
#     return render(request, 'authentication/login.html')


class UsernameValidation(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain letters and numbers'}, status=400)
        # if usrname exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username already exsits.. try another one'}, status=409)

        return JsonResponse({'username_valid': True})


class EmailValidation(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error': 'invalid email'}, status=400)
        # if usrname exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'email already exsits.. try another one'}, status=409)

        return JsonResponse({'email_valid': True})
