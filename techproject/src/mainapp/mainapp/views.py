from django.shortcuts import render

def home(request):
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    context = {
        'user': request.user,
        'products': products,
    }
    return render(request, "home.html", context)