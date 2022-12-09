from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages

# Create your views here.


@login_required(login_url='/authentication/login')
def home(request):
    categories = Category.objects.all()
    return render(request, 'expenses/index.html')


def base(request):
    return render(request, 'expenses/base.html')


# def add_expense(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         context = {
#             'categories': categories,
#             'values': request.POST
#         }
#         return render(request, 'expenses/add_expense.html', context)

#     if request.method == 'POST':
#         amount = request.POST['amount']
#         description = request.POST['description']
#         if not amount:
#             messages.error(request, 'amount is required')
#         elif not description:
#             messages.error(request, 'description is required')

#         categories = Category.objects.all()
#         context = {
#             'categories': categories,
#             'values': request.POST
#         }
#         return render(request, 'expenses/add_expense.html', context)
def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        if not amount:
            messages.error(request, 'amount is required')
        elif not description:
            messages.error(request, 'description is required')
        return render(request, 'expenses/add_expense.html', context)
