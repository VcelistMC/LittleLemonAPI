from django.shortcuts import get_object_or_404
from rest_framework import serializers

from cart.models import Cart, CartItem
from core.models import LittleLemonUser
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

class CartItemPostRequestSerializer(serializers.Serializer):
    itemId = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)

    def validate_itemId(self, id):
        v = get_object_or_404(MenuItem, pk=id)
        print(v)
        if v is MenuItem.DoesNotExist:
            raise serializers.ValidationError("Menu item not found")

        return id

    def save(self, userId):
        _itemId = self.validated_data['itemId']
        _quantity = self.validated_data['quantity']
        print(self.validated_data)

        item = MenuItem.objects.get(pk=_itemId)
        currentCart, _ = Cart.objects.get_or_create(user__id=userId)

        return CartItem(cart=currentCart, menuItem=item, quantity=_quantity).save()

    

