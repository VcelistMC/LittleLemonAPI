from django.shortcuts import get_object_or_404
from rest_framework import serializers

from cart.models import Cart, CartItem
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
    itemId = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)

    def validate_itemId(self, id):
        get_object_or_404(MenuItem, pk=id)

        return id

    def save(self, userId):
        _itemId = self.validated_data['itemId']
        _quantity = self.validated_data['quantity']

        item = MenuItem.objects.get(pk=_itemId)
        currentCart, _ = Cart.objects.get_or_create(user__id=userId)

        createdItem = CartItem(cart=currentCart, menuItem=item, quantity=_quantity)
        createdItem.save()

        return createdItem

    

