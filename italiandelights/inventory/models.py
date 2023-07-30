from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class MenuItem(models.Model):
    title = models.CharField(max_length=75)
    price = models.FloatField(help_text="Enter the menu price")
    ingredients = models.ManyToManyField(Ingredient, through='MenuItemIngredient')

    def __str__(self):
        return f"{self.title}"

class MenuItemIngredient(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"{self.menu_item.title} - {self.ingredient.name} - {self.quantity}"

    
class Order(models.Model):
    menu_items = models.ManyToManyField(MenuItem)
    timestamp = models.DateTimeField(auto_now_add=True)
