from django import forms
from .models import Ingredient, MenuItem, Order

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["menu_items"]      

