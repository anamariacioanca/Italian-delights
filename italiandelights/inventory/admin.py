from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, Recipe, Order

# class RecipeIngredientInline(admin.TabularInline):
#     model = Recipe.ingredients.through

# class RecipeAdmin(admin.ModelAdmin):
#     inlines = [RecipeIngredientInline]

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Recipe)
admin.site.register(Order)

