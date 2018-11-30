from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    user = request.user
    context = {
        'user': user,
        'products': products,
    }
    return render(request, "home.html", context)
