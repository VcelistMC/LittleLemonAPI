from django.shortcuts import get_object_or_404
from rest_framework import serializers

from cart.models import Cart, CartItem
from core.services import get_object_or_none
from menu.models import MenuItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'quantity', 'total', 'menuItem']
        depth=1

    @staticmethod
    def serialize(item, many=False):
        itemSerial = CartItemSerializer(item, many=many)
        return itemSerial.data

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, source='cart')
    class Meta:
        model = Cart
        fields = ['user', 'cartTotal', 'items']

    @staticmethod
    def serialize(cart, many=False):
        cartSerializer = CartSerializer(cart, many=many)
        return cartSerializer.data

class CartItemPostRequestSerializer(serializers.Serializer):
    item = serializers.PrimaryKeyRelatedField(required=True, queryset=MenuItem.objects.all())
    quantity = serializers.IntegerField(required=True)


    def save(self, userId):
        _item = self.validated_data['item']
        _quantity = self.validated_data['quantity']
        currentCart, _ = Cart.objects.get_or_create(user__id=userId)
        createdItem = CartItem(cart=currentCart, menuItem=_item, quantity=_quantity)
        createdItem.save()
        return createdItem

    

