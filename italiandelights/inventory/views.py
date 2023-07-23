from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.db.models import Sum
from .models import Ingredient, MenuItem, Order, Recipe
# Create your views here.

def inventory_view(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/inventory.html', {'ingredients': ingredients})

def orders_view(request):
    orders = Order.objects.all()
    return render(request, 'inventory/orders.html', {'orders': orders})

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'inventory/menu.html', {'menu_items': menu_items})

def recipe_view(request):
    recipe = Recipe.objects.all()
    return render(request, 'inventory/recipe.html', {'recipe': recipe})

def total_sales_view(request):
    total_sales = Order.objects.aggregate(Sum('menu_items__price'))['menu_items__price__sum']
    return render(request, 'inventory/total_sales.html', {'total_sales': total_sales})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")  # Redirect on successful login
            else:
                # Invalid credentials, display an error message
                error_message = "Invalid credentials. Please try again."
                return render(request, "inventory/login.html", {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()    
    context = {
        "form": form
    }
    return render(request, "inventory/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/")

def main_view(request):
    return render(request, "inventory/base.html", {})