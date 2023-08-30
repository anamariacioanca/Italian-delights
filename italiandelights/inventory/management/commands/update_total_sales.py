from django.core.management.base import BaseCommand
from datetime import date
from inventory.models import TotalSales

class Command(BaseCommand):
    help = 'Update TotalSales instances'

    def handle(self, *args, **options):
        today = date.today()
        total_sales, created = TotalSales.objects.get_or_create(date=today)
        total_sales.update_totals()
        self.stdout.write(self.style.SUCCESS('TotalSales instances updated successfully'))
