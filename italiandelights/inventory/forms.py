from django import forms
from .models import Ingredient, MenuItem

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["title", "price"]         