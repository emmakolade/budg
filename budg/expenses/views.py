from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/authentication/login')
def home(request):
    return render(request, 'expenses/index.html')


def base(request):
    return render(request, 'expenses/base.html')


def add_expense(request):
    return render(request, 'expenses/add_expense.html')

# def login(request):
#     return render(request, 'expenses/login.html')

# def register(request):
#     return render(request, 'expenses/register.html')
