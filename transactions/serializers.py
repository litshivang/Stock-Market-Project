# transactions/serializers.py

from rest_framework import serializers
from .models import BuyTransaction, SellTransaction, SplitTransaction

class BuyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyTransaction
        fields = '__all__'

class SellTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellTransaction
        fields = '__all__'

class SplitTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitTransaction
        fields = '__all__'
