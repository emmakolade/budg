from django.shortcuts import render
from django.views import View
# Create your views here.

class Registration(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

class Login(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
