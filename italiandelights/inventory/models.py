from django.db import models
from django.db.models import Sum

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
    
class Order(models.Model):
    menu_items = models.ManyToManyField(MenuItem)
    timestamp = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first
        self.total_price = self.calculate_total_price()  # Calculate and set total price
        super().save(*args, **kwargs)  # Save again to update total_price

        # Update TotalSales instance
        total_sales, created = TotalSales.objects.get_or_create(date=self.timestamp.date())
        total_sales.update_totals()

    def calculate_total_price(self):
        return sum(menu_item.price for menu_item in self.menu_items.all())

class TotalSales(models.Model):
    date = models.DateField(unique=True)
    total_order_price = models.FloatField(default=0)
    total_all_orders_price = models.FloatField(default=0)

    def __str__(self):
        return f"Total Sales for {self.date}"

    def update_totals(self):
        orders_on_date = Order.objects.filter(timestamp__date=self.date)
        self.total_order_price = sum(order.total_price for order in orders_on_date)
        self.total_all_orders_price = TotalSales.objects.aggregate(Sum('total_order_price'))['total_order_price__sum'] or 0
        self.save()



       

