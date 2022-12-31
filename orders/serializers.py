from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['quantity', 'total', 'menuItem']
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source = "order")
    class Meta:
        model = Order
        fields = ['id', 'customer', 'orderTotal', 'delivery_crew', 'status', 'items']

    @staticmethod
    def serialize(model, many=False):
        return OrderSerializer(model, many=many).data