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

    def __str__(self):
        return f"{self.title}"
        

class Recipe(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    quantity = models.PositiveIntegerField(default=1)
    unit = models.CharField(max_length=10, null=True, blank=True)
    
class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
