from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'expenses/index.html')

def add_expense(request):
    return render(request, 'expenses/add_expense.html')

# def login(request):
#     return render(request, 'expenses/login.html')

# def register(request):
#     return render(request, 'expenses/register.html')