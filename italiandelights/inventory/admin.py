from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, Recipe, Order

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Recipe)
admin.site.register(Order)

