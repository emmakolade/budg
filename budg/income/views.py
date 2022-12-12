from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Source, Income
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
# Create your views here.


@login_required(login_url='/authentication/login')
def home(request):
    sources = Source.objects.all()
    income = Income.objects.filter(user=request.user).order_by('-date')
    context = {
        'income': income,
    }
    return render(request, 'income/index.html', context)


def add_income(request):
    if request.method == 'GET':
        sources = Source.objects.all()
        context = {'sources': sources}
        return render(request, 'income/add_income.html', context)

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
        return redirect('add_income')

    # Retrieve the date and category from the request data
    date = request.POST.get('date')
    source = request.POST.get('source')

    # Create a new Expense object with the given data
    Income.objects.create(user=request.user, amount=amount,
                          date=date, source=source, description=description)
    messages.success(request, 'income source saved succesfully')
    return redirect('income')


def edit_income(request, id):
    # Get the expense to be edited
    income = Income.objects.get(pk=id)

    # Get all available categories
    sources = Source.objects.all()

    if request.method == 'POST':
        # Get the amount, description, and source from the request
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        source = request.POST.get('source')

        # Check if the amount and description are present
        if not amount or not description:
            messages.error(request, 'amount and description are required')
            return redirect('edit_income')

        # Update the expense with the new values
        income.amount = amount
        income.source = source
        income.description = description
        income.save()
        messages.success(request, ' income upadted succesfully')
        return redirect('income')

    context = {
        'income': income,
        'values': income,
        'source': sources,
    }

    return render(request, 'income/edit_income.html', context)


def delete_income(request, id):
    income = Income.objects.get(pk=id)
    income.delete()
    messages.success(request, 'Income record deleted successfully')
    return redirect('home')


# def search_expense(request):
#     if request.method == "POST":
#         search_request = json.loads(request.body).get('searchText')

#         s_expenses = Expense.objects.filter(amount__starts_with=search_request, user=request.user) | Expense.objects.filter(
#             date__starts_with=search_request, user=request.user) | Expense.objects.filter(description__icontains=search_request, user=request.user) | Expense.objects.filter(category__icontians=search_request, user=request.user)

#         data = s_expenses.values()

#         return JsonResponse(list(data), safe=False)
