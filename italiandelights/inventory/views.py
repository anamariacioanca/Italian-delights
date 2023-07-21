from django.shortcuts import render
from django.db.models import Sum
from .models import Ingredient, MenuItem, Order, Recipe
# Create your views here.

def inventory_view(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory.html', {'ingredients': ingredients})

def orders_view(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def total_sales_view(request):
    total_sales = Order.objects.aggregate(Sum('menu_items__price'))['menu_items__price__sum']
    return render(request, 'total_sales.html', {'total_sales': total_sales})
