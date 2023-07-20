from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=10)

class MenuItem(models.Model):
    title = models.CharField(max_length=75)
    price = models.FloatField(help_text="Enter the menu price")

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="Enter the amount of ingredient required to create the menu item")      

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
