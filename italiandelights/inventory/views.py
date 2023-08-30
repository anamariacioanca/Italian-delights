from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import LoginForm, IngredientForm, MenuItemForm, OrderForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredient, MenuItem, Order, TotalSales
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class IngredientList(ListView):
  model = Ingredient
  template_name = "inventory/ingredients.html"

@method_decorator(login_required, name='dispatch')
class IngredientCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'inventory.add_ingredient'
  model = Ingredient
  template_name = "inventory/ingredient_create_form.html"
  form_class = IngredientForm
  success_url = reverse_lazy("ingredients")

@method_decorator(login_required, name='dispatch')
class IngredientUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'inventory.edit_ingredient'
  model = Ingredient
  template_name = "inventory/ingredient_update_form.html"  
  fields = ["quantity"]  
  success_url = reverse_lazy("ingredients")

@method_decorator(login_required, name='dispatch')
class IngredientDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'inventory.delete_ingredient'
  model = Ingredient
  template_name = "inventory/ingredient_delete_form.html"  
  success_url = reverse_lazy("ingredients")

class MenuItemList(ListView):
  model = MenuItem
  template_name = "inventory/menuitem.html"

@method_decorator(login_required, name='dispatch')
class MenuItemCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'inventory.add_menuitem'
  model = MenuItem
  template_name = "inventory/menuitem_create_form.html"
  form_class = MenuItemForm
  success_url = reverse_lazy("menuitems")

@method_decorator(login_required, name='dispatch')   
class MenuItemUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'inventory.edit_menuitem'
  model = MenuItem
  template_name = "inventory/menuitem_update_form.html"
  form_class = MenuItemForm
  success_url = reverse_lazy("menuitems")

@method_decorator(login_required, name='dispatch')
class MenuItemDelete(PermissionRequiredMixin, DeleteView):
  permission_required = 'inventory.delete_menuitem'
  model = MenuItem
  template_name = "inventory/menuitem_delete_form.html"  
  success_url = reverse_lazy("menuitems")

class OrderList(ListView):
  model = Order
  template_name = "inventory/orders.html"

class OrderCreate(CreateView):
  model = Order
  template_name = "inventory/order_create_form.html"
  fields = ["menu_items"]
  success_url = reverse_lazy("orders")

  def form_valid(self, form):
        order = form.save(commit=False)  
        order.save() 
        
        selected_menu_items_ids = self.request.POST.getlist('menu_items')
        selected_menu_items = MenuItem.objects.filter(pk__in=selected_menu_items_ids)
        order.menu_items.set(selected_menu_items)  
        
        order.total_price = order.calculate_total_price() 
        order.save()  
        
        return super().form_valid(form)

class OrderUpdate(UpdateView):
  model = Order
  template_name = "inventory/order_update_form.html"  
  fields = ["menu_items"]  
  success_url = reverse_lazy("orders")

class OrderDelete(DeleteView):
  model = Order
  template_name = "inventory/order_delete_form.html"  
  success_url = reverse_lazy("orders")

@method_decorator(login_required, name='dispatch')
class TotalSalesList(PermissionRequiredMixin, ListView):
  permission_required = 'inventory.view_totalsales'
  model = TotalSales
  template_name = "inventory/total_sales.html"
    
  def get_queryset(self):
      return TotalSales.objects.order_by("-date")

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

@login_required(login_url='login')
def main_view(request):
    return render(request, "inventory/base.html", {})