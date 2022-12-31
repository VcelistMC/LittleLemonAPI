from rest_framework import serializers

from core.models import LittleLemonUser, UserGroups
from .models import Order, OrderItem, OrderStatus

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


class OrderManagerPatchRequest(serializers.Serializer):
    delivery_crew = serializers.PrimaryKeyRelatedField(queryset = LittleLemonUser.objects.all(), required=False, default=None)
    status = serializers.ChoiceField(choices=OrderStatus.choices, required=False, default=None)

    def validate_delivery_crew(self, user):
        if user is None: return None

        if not user.belongsToGroup(UserGroups.DELIVERY_CREW):
            raise serializers.ValidationError(f'User {user} is not a delivery crew')
        return user

    def save(self, order: Order):
        _crew = self.validated_data['delivery_crew']
        _status = self.validated_data['status']

        if _crew:
            order.assignToCrew(_crew)
        
        if _status:
            order.status = _status

        order.save()

        return order

class OrderDeliveryPatchRequest(serializers.Serializer):
    status = serializers.ChoiceField(choices=OrderStatus.choices, required=True)

    def save(self, order: Order):
        _status = self.validated_data['status']
        
        if _status:
            order.status = _status

        order.save()

        return order


