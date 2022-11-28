from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'store/index.html')

def add_expense(request):
    return render(request, 'store/add_expense.html')

def login(request):
    return render(request, 'store/login.html')

def register(request):
    return render(request, 'store/register.html')