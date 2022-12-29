from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cart.models import CartItem
from core.models import LittleLemonUser

from orders.models import Order
from orders.serializers import OrderSerializer

class OwnOrdersGetCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        currentUserOrders = Order.objects.filter(customer__pk=request.user.id)
        print(type(request.user))

        return Response(OrderSerializer.serialize(currentUserOrders, True))

    # this request takes an avg of 11 seconds to complete bruh lmao fix it
    def post(self, request, *args, **kwargs):
        currentUser = request.user

        newOrder = Order(customer=currentUser)
        currentCartItems = CartItem.objects.filter(cart__user = currentUser)
        newOrder.save()

        for item in currentCartItems:
            orderItem = item.toOrderItem(newOrder)
            orderItem.save()
            item.delete()
        

        return Response(OrderSerializer.serialize(newOrder), status=201)
        

