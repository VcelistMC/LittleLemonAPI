from rest_framework import serializers

from cart.models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity', 'menuItem']
        depth = 1

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