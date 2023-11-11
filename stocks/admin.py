# stocks/admin.py

from django.contrib import admin
from .models import Stock
#adminregister
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('company', 'quantity', 'average_buy_price')
