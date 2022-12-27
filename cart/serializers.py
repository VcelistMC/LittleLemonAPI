from rest_framework import serializers

from cart.models import Cart, CartItem
from menu.models import MenuItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity', 'menuItem']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, source='cart')
    class Meta:
        model = Cart
        fields = '__all__'

    @staticmethod
    def serialize(cart, many=False):
        cartSerializer = CartSerializer(cart, many)
        cartSerializer.is_valid()
        return cartSerializer.data

class CartItemPostRequestSerializer(serializers.ModelSerializer):
    menuItem = serializers.PrimaryKeyRelatedField(required=True, queryset=MenuItem.objects.all())
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = CartItem
        fields = ['quantity', 'menuItem']

