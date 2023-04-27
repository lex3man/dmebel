from rest_framework import serializers
from .models import Contract, PreOrder, Order
from ..res.serializers import ClientSerializer


class ContractSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        # fields = ['caption', 'number', 'date', 'amount']
        exclude = []


class PreOrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = PreOrder
        # fields = ['caption', 'client', 'details']
        exclude = []


class OrderSerializer(serializers.ModelSerializer):
    preorder = PreOrderSerializer(read_only=True)
    class Meta:
        model = Order
        # fields = ['caption', 'client', 'details', 'preorder', 'status', 'prod_type', 'contract']
        exclude = []
