from django.shortcuts import render
from .models import Dish
from django.http import HttpResponse
def search(request):
    print(request)
    query = request.GET.get('q')  # Get the search query from the request
    print("query",query)
    if query:
        dishes = Dish.objects.filter(name__icontains=query)  # Perform a case-insensitive search
    else:
        dishes = Dish.objects.none()  # Return an empty queryset if no query is provided
    return render(request, 'search_app/search.html',{'dishes': dishes, 'query': query ,})
def greet(request):
    return render(request,'search_app/index.html')
   