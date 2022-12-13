from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
import datetime
# Create your views here.


@login_required(login_url='/authentication/login')
def home(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(user=request.user).order_by('-date')

    # paginator = Paginator(expenses, 5)
    # page_number = request.GET.get('page')
    # # page_object = paginator.page(page_number)
    # page_object = Paginator.get_page(paginator, page_number)
    context = {
        'expenses': expenses,
        # 'page_object': page_object,
    }
    return render(request, 'expenses/index.html', context)


def base(request):
    return render(request, 'expenses/base.html')


def add_expense(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'expenses/add_expense.html', context)

    # If the request method is not GET, it must be POST
    # Retrieve the amount from the request data
    amount = request.POST.get('amount')
    # If no amount was provided, add an error message and redirect
    if not amount:
        messages.error(request, 'amount is required')
        return redirect('add_expense')

    # Retrieve the description from the request data
    description = request.POST.get('description')
    # If no description was provided, add an error message and redirect
    if not description:
        messages.error(request, 'description is required')
        return redirect('add_expense')

    # Retrieve the date and category from the request data
    date = request.POST.get('date')
    category = request.POST.get('category')

    # Create a new Expense object with the given data
    Expense.objects.create(user=request.user, amount=amount,
                           date=date, category=category, description=description)
    messages.success(request, 'new expense saved succesfully')
    return redirect('home')


def edit_expense(request, id):
    # Get the expense to be edited
    expense = Expense.objects.get(pk=id)

    # Get all available categories
    categories = Category.objects.all()

    if request.method == 'POST':
        # Get the amount, description, and category from the request
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        category = request.POST.get('category')

        # Check if the amount and description are present
        if not amount or not description:
            messages.error(request, 'amount and description are required')
            return redirect('edit_expense')

        # Update the expense with the new values
        expense.user = request.user
        expense.amount = amount
        expense.category = category
        expense.description = description
        expense.save()
        messages.success(request, ' expense upadted succesfully')
        return redirect('home')

    context = {
        'expense': expense,
        'values': expense,
        'categories': categories,
    }

    return render(request, 'expenses/edit_expense.html', context)

# def edit_expense(request, id):
#     expense = Expense.objects.get(pk=id)
#     categories = Category.objects.all()
#     context = {
#         'expense': expense,
#         'values': expense,
#         'categories': categories,
#     }
#     if request.method == 'GET':
#         return render(request, 'expenses/edit_expense.html', context)
#     amount = request.POST.get('amount')
#     if not amount:
#         messages.error(request, 'amount is required')
#         return redirect('edit_expense')

#     description = request.POST.get('description')
#     if not description:
#         messages.error(request, 'description is required')
#         return redirect('edit_expense')

#     # date = request.POST.get('date')
#     category = request.POST.get('category')
#     expense.user = request.user
#     expense.amount = amount
#     expense.category = category
#     expense.description = description
#     expense.save()

#     messages.success(request, ' expense upadted succesfully')
#     return redirect('home')


def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'deleted successfully')
    return redirect('home')


def search_expense(request):
    if request.method == "POST":
        search_request = json.loads(request.body).get('searchText')

        s_expenses = Expense.objects.filter(amount__starts_with=search_request, user=request.user) | Expense.objects.filter(
            date__starts_with=search_request, user=request.user) | Expense.objects.filter(description__icontains=search_request, user=request.user) | Expense.objects.filter(category__icontians=search_request, user=request.user)

        data = s_expenses.values()

        return JsonResponse(list(data), safe=False)

# endpoint visualizing the expense data


def expense_summary(request):
    current_date = datetime.date.today()
    sixmonth_ago = current_date - datetime.timedelta(days=30 * 6)
    expenses_date = Expense.objects.filter(user=request.user,
                                           date__gte=sixmonth_ago, date_lte=current_date)

    finalrep = {}

    # get all the category in an expense
    def get_category(expense):
        return expense.category

    category_list = list(set(map(get_category, expenses_date)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_category = expenses_date.filter(category=category)
        for item in filtered_category:
            amount += item.amount
        return amount

    for x in expenses_date:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)

    return JsonResponse({'expense_category_data': finalrep}, safe=False)


def expense_stats(request):
    return render(request, 'expenses/expense_stats.html')


def income_stats(request):
    return render(request, 'expenses/income_stats.html')
