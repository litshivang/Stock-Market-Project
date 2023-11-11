# transactions/admin.py

from django.contrib import admin
from .models import BuyTransaction, SellTransaction, SplitTransaction

@admin.register(BuyTransaction)
class BuyTransactionAdmin(admin.ModelAdmin):
    list_display = ('company', 'quantity', 'price_per_share', 'date')

@admin.register(SellTransaction)
class SellTransactionAdmin(admin.ModelAdmin):
    list_display = ('company', 'quantity', 'price_per_share', 'date')

@admin.register(SplitTransaction)
class SplitTransactionAdmin(admin.ModelAdmin):
    list_display = ('company', 'display_split_ratio', 'date')

    def display_split_ratio(self, obj):
        return obj.split_ratio

    display_split_ratio.short_description = 'Split Ratio'
