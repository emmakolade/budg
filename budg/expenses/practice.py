# paginator = Paginator(expenses, 5)
# page_number = request.GET.get('page')
# # page_object = paginator.page(page_number)
# page_object = Paginator.get_page(paginator, page_number)

# 'page_object': page_object,


# def search_expense(request):
#     if request.method == "POST":
#         search_request = json.loads(request.body).get('searchText')

#         s_expenses = Expense.objects.filter(amount__starts_with=search_request, user=request.user) | Expense.objects.filter(
#             date__starts_with=search_request, user=request.user) | Expense.objects.filter(description__icontains=search_request, user=request.user) | Expense.objects.filter(category__icontians=search_request, user=request.user)

#         data = s_expenses.values()

#         return JsonResponse(list(data), safe=False)
