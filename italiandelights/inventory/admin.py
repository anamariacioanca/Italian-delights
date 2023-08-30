from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, Order, TotalSales

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(TotalSales)

