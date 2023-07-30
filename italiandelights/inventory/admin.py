from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, Order

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Order)

