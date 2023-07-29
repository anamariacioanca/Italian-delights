from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import LoginForm, IngredientForm
from django.db.models import Sum
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredient, MenuItem, Order, Recipe
# Create your views here.

# def inventory_view(request):
#     ingredients = Ingredient.objects.all()
#     return render(request, 'inventory/inventory.html', {'ingredients': ingredients})


class IngredientList(ListView):
  model = Ingredient
  template_name = "inventory/ingredients.html"

class IngredientCreate(CreateView):
  model = Ingredient
  template_name = "inventory/ingredient_create_form.html"
  form_class = IngredientForm
  success_url = reverse_lazy("ingredients")
  
class IngredientUpdate(UpdateView):
  model = Ingredient
  template_name = "inventory/ingredient_update_form.html"  
  fields = ["quantity"]  
  success_url = reverse_lazy("ingredients")

class IngredientDelete(DeleteView):
  model = Ingredient
  template_name = "inventory/ingredient_delete_form.html"  
  success_url = reverse_lazy("ingredients")

# def menu_view(request):
#     menu_items = MenuItem.objects.all()
#     return render(request, 'inventory/menu.html', {'menu_items': menu_items})

class MenuItemList(ListView):
  model = MenuItem
  template_name = "inventory/menuitem.html"

class MenuItemCreate(CreateView):
  model = MenuItem
  template_name = "inventory/menuitem_create_form.html"
  fields = ["title", "price"]  

class MenuItemUpdate(UpdateView):
  model = MenuItem
  template_name = "inventory/menuitem_update_form.html"  

class MenuItemDelete(DeleteView):
  model = MenuItem
  template_name = "inventory/menuitem_delete_form.html"  

# def recipe_view(request):
#     recipe = Recipe.objects.all()
#     return render(request, 'inventory/recipe.html', {'recipe': recipe})

class RecipeList(ListView):
  model = Recipe
  template_name = "inventory/recipes.html"

class RecipeCreate(CreateView):
  model = Recipe
  template_name = "inventory/recipe_create_form.html"
  fields = ["menu_item", "ingredient", "quantity", "unit"]  

class RecipeUpdate(UpdateView):
  model = Recipe
  template_name = "inventory/recipe_update_form.html"  

class RecipeDelete(DeleteView):
  model = Recipe
  template_name = "inventory/recipe_delete_form.html"  

# def orders_view(request):
#     orders = Order.objects.all()
#     return render(request, 'inventory/orders.html', {'orders': orders})

class OrderList(ListView):
  model = Order
  template_name = "inventory/orders.html"

class OrderCreate(CreateView):
  model = Order
  template_name = "inventory/order_create_form.html"
  fields = ["menu_items", "timestamp"]  

class OrderUpdate(UpdateView):
  model = Order
  template_name = "inventory/order_update_form.html"  

class OrderDelete(DeleteView):
  model = Order
  template_name = "inventory/order_delete_form.html"  

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