# transactions/models.py

from django.db import models

class BuyTransaction(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=255)
    trade_type = models.CharField(max_length=4, default='BUY')
    quantity = models.PositiveIntegerField()
    price_per_share = models.DecimalField(max_digits=10, decimal_places=2)

class SellTransaction(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=255)
    trade_type = models.CharField(max_length=4, default='SELL')
    quantity = models.PositiveIntegerField()
    price_per_share = models.DecimalField(max_digits=10, decimal_places=2)

class SplitTransaction(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=255)
    trade_type = models.CharField(max_length=5, default='SPLIT')

class Stock(models.Model):
    company = models.CharField(max_length=255, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    average_buy_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

