from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


@login_required(login_url='/authentication/login')
def home(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(user=request.user)
    paginator=Paginator(expenses, 4 )
    page_number = request.GET.get('page')
    page_object = Paginator.get_page(paginator, page_number)
    context = {
        'expenses': expenses,
        'page_object': page_object
    }
    return render(request, 'expenses/index.html', context)


def base(request):
    return render(request, 'expenses/base.html')


def add_expense(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'expenses/add_expense.html', context)

    amount = request.POST.get('amount')
    if not amount:
        messages.error(request, 'amount is required')
        return redirect('add_expense')

    description = request.POST.get('description')
    if not description:
        messages.error(request, 'description is required')
        return redirect('add_expense')

    date = request.POST.get('date')
    category = request.POST.get('category')
    Expense.objects.create(user=request.user, amount=amount,
                           date=date, category=category, description=description)
    messages.success(request, 'new expense save succesfully')
    return redirect('home')


# def add_expense(request):
#     categories = Category.objects.all()
#     context = {
#         'categories': categories,
#         'values': request.POST
#     }

#     if request.method == 'GET':
#         return render(request, 'expenses/add_expense.html', context)

#     if request.method == 'POST':
#         amount = request.POST.get('amount')
#         if not amount:
#             messages.error(request, 'amount is required')
#             return render(request, 'expenses/add_expense.html', context)
#         description = request.POST.get('description')
#         date = request.POST['date']
#         category = request.POST['category']

#         if not description:
#             messages.error(request, 'description is required')
#             return render(request, 'expenses/add_expense.html', context)

#         Expense.objects.create(user=request.user, amount=amount, date=date,
#                                category=category, description=description)
#         messages.success(request, 'new expense save succesfully')
#         return redirect('home')

def edit_expense(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'expense': expense,
        'values': expense,
        'categories': categories,
    }
    if request.method == 'GET':
        return render(request, 'expenses/edit_expense.html', context)
    amount = request.POST.get('amount')
    if not amount:
        messages.error(request, 'amount is required')
        return redirect('edit_expense')

    description = request.POST.get('description')
    if not description:
        messages.error(request, 'description is required')
        return redirect('edit_expense')

    date = request.POST.get('date')
    category = request.POST.get('category')
    expense.user = request.user
    expense.amount = amount
    expense.date = date
    expense.category = category
    expense.description = description
    expense.save()

    messages.success(request, ' expense upadted succesfully')
    return redirect('home')


def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'deleted successfully')
    return redirect('home')
