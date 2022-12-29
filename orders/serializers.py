from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'orderTotal', 'status']

    @staticmethod
    def serialize(model, many=False):
        return OrderSerializer(model, many=many).data