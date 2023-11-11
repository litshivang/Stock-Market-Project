# stocks/models.py

from django.db import models

class Stock(models.Model):
    company = models.CharField(max_length=255, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    average_buy_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
