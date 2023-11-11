# transactions/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import BuyTransaction, SellTransaction, SplitTransaction
from .serializers import BuyTransactionSerializer, SellTransactionSerializer, SplitTransactionSerializer
from stocks.models import Stock

class BuyTransactionListCreateView(generics.ListCreateAPIView):
    queryset = BuyTransaction.objects.all()
    serializer_class = BuyTransactionSerializer

    def perform_create(self, serializer):        
        transaction = serializer.save(user=self.request.user if self.request.user.is_authenticated else None)

        # Calculate average buy price and update balance quantity
        self.update_stock_info(transaction)

    def update_stock_info(self, buy_transaction):
        company = buy_transaction.company
        quantity = buy_transaction.quantity
        price_per_share = buy_transaction.price_per_share

        # Assuming you have a Stock model for tracking stock information
        stock, created = Stock.objects.get_or_create(company=company)

        # Calculate average buy price and update balance quantity
        total_quantity = stock.quantity + quantity
        stock.average_buy_price = (
            (stock.average_buy_price * stock.quantity) + (price_per_share * quantity)
        ) / total_quantity
        stock.quantity += quantity
        stock.save()

class SellTransactionListCreateView(generics.ListCreateAPIView):
    queryset = SellTransaction.objects.all()
    serializer_class = SellTransactionSerializer

    def perform_create(self, serializer):
        transaction = serializer.save(user=self.request.user if self.request.user.is_authenticated else None)

        # Calculate average buy price and update balance quantity
        self.update_stock_info(transaction)

    def update_stock_info(self, sell_transaction):
        company = sell_transaction.company
        quantity_to_sell = sell_transaction.quantity

        # Assuming you have a Stock model for tracking stock information
        stock, created = Stock.objects.get_or_create(company=company)

        # Retrieve all buy transactions for the given company, ordered by date
        buy_transactions = BuyTransaction.objects.filter(company=company).order_by('date')

        # Calculate the total quantity bought and deduct sold quantity based on FIFO
        total_quantity_bought = sum([buy.quantity for buy in buy_transactions])
        remaining_quantity_to_sell = quantity_to_sell

        for buy_transaction in buy_transactions:
            if remaining_quantity_to_sell > 0:
                if remaining_quantity_to_sell >= buy_transaction.quantity:
                    # Sell all stocks from this buy transaction
                    remaining_quantity_to_sell -= buy_transaction.quantity
                    buy_transaction.quantity = 0
                    buy_transaction.save()
                else:
                    # Sell part of the stocks from this buy transaction
                    buy_transaction.quantity -= remaining_quantity_to_sell
                    buy_transaction.save()
                    remaining_quantity_to_sell = 0

        # Update the stock's quantity and average buy price
        stock.quantity -= quantity_to_sell
        stock.save()

        # Calculate average buy price
        if total_quantity_bought > 0:
            stock.average_buy_price = sum([buy.price_per_share * buy.quantity for buy in buy_transactions]) / total_quantity_bought
        else:
            stock.average_buy_price = 0.0

        stock.save()

class SplitTransactionListCreateView(generics.ListCreateAPIView):
    queryset = SplitTransaction.objects.all()
    serializer_class = SplitTransactionSerializer

    def perform_create(self, serializer):
        transaction = serializer.save()

        # Handle split transaction logic
        self.handle_split_transaction(transaction)

    def handle_split_transaction(self, split_transaction):
        company = split_transaction.company
        split_ratio = split_transaction.split_ratio

        # Assuming you have a Stock model for tracking stock information
        stock, created = Stock.objects.get_or_create(company=company)

        # Update stock information based on the split ratio
        stock.quantity *= split_ratio
        stock.average_buy_price /= split_ratio
        stock.save()
