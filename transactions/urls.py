# transactions/urls.py

from django.urls import path
from .views import BuyTransactionListCreateView, SellTransactionListCreateView, SplitTransactionListCreateView

urlpatterns = [
    path('buy/', BuyTransactionListCreateView.as_view(), name='buy-transaction-list-create'),
    path('sell/', SellTransactionListCreateView.as_view(), name='sell-transaction-list-create'),
    path('split/', SplitTransactionListCreateView.as_view(), name='split-transaction-list-create'),
]
