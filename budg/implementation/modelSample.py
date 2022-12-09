# Import the required modules
from django.http import HttpResponseRedirect
from django.conf import settings
import requests
from django.db import models
import django
import datetime

# Set up Django
django.setup()

# Import the models we will use from Django's ORM

# Define a model for a transaction


class Transaction(models.Model):
    # The transaction date
    date = models.DateField()
    # The transaction description
    description = models.CharField(max_length=255)
    # The transaction amount
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # The transaction type (e.g. debit or credit)
    transaction_type = models.CharField(max_length=255)

# Define a model for a budget


class Budget(models.Model):
    # The budget start date
    start_date = models.DateField()
    # The budget end date
    end_date = models.DateField()
    # The budget amount
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # The transactions that are part of this budget
    transactions = models.ManyToManyField(Transaction)

# Create a function to calculate the total amount spent in a given budget


def calculate_total_spent(budget):
    # Initialize a variable to track the total amount spent
    total_spent = 0

    # Loop through the transactions in the budget
    for transaction in budget.transactions.all():
        # If the transaction is a debit, add the amount to the total spent
        if transaction.transaction_type == "debit":
            total_spent += transaction.amount

    # Return the total amount spent
    return total_spent

# Create a function to calculate the remaining budget for a given budget


def calculate_remaining_budget(budget):
    # Get the total amount spent in the budget
    total_spent = calculate_total_spent(budget)

    # Calculate the remaining budget by subtracting the total spent from the budget amount
    remaining_budget = budget.amount - total_spent

    # Return the remaining budget
    return remaining_budget

# Create a function to add a new transaction to a budget


def add_transaction(budget, date, description, amount, transaction_type):
    # Create a new transaction
    transaction = Transaction(date=date, description=description,
                              amount=amount, transaction_type=transaction_type)
    # Save the transaction to the database
    transaction.save()
    # Add the transaction to the budget
    budget.transactions.add(transaction)
    # Save the budget
    budget.save()

# Create a function to create a new budget


def create_budget(start_date, end_date, amount):
    # Create a new budget
    budget = Budget(start_date=start_date, end_date=end_date, amount=amount)
    # Save the budget to the database
    budget.save()
    # Return the budget
    return budget


# Create a new budget for the current month
current_month_start = datetime.date.today().replace(day=1)
current_month_end = datetime.date.today().replace(day=cal)


# Import the necessary modules
import datetime

# Import Django's ORM
from django.db import models

# Define a Django model for expenses
class Expense(models.Model):
  # Define fields for the model
  date = models.DateField()
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.CharField(max_length=100)
  description = models.TextField()
  
  # Define a method to return a string representation of the model
  def __str__(self):
    return '{} - {} ({})'.format(self.date, self.amount, self.category)

# Define a Django view to display a list of expenses
def expense_list(request):
  # Query the database to get a list of all expenses
  expenses = Expense.objects.all()
  
  # Return a response to the request, including the list of expenses
  return render(request, 'expenses/list.html', {'expenses': expenses})

# Define a Django view to add a new expense
def expense_add(request):
  # Check if the request is a POST request (i.e. the user has submitted the form)
  if request.method == 'POST':
    # Bind the form data to a form object
    form = ExpenseForm(request.POST)
    
    # Check if the form data is valid
    if form.is_valid():
      # Save the new expense to the database
      expense = form.save()
      
      # Redirect the user to the expense list page
      return redirect('expense_list')
      
  # If the request is not a POST request, or the form data is not valid,
  # render the form template to display the form
  return render(request, 'expenses/add.html', {'form': ExpenseForm()})


