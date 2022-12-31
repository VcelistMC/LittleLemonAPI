from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cart.models import CartItem
from rest_framework.generics import RetrieveDestroyAPIView
from core.mixins import MultipleLookUpFieldMixin
from orders.models import Order
from orders.serializers import OrderSerializer
import threading

class OwnOrdersGetCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        currentUserOrders = Order.objects.filter(customer__pk=request.user.id)
        return Response(OrderSerializer.serialize(currentUserOrders, True))

    def deleteRelatedCartItems(self, items):
        for item in items:
            item.delete()
        print("All items deleted")

    def post(self, request, *args, **kwargs):
        currentUser = request.user

        newOrder = Order(customer=currentUser)
        currentCartItems = CartItem.objects.filter(cart__user = currentUser)
        newOrder.save()

        for item in currentCartItems:
            orderItem = item.toOrderItem(newOrder)
            orderItem.save()

        # user doesn't care about item deletion so we start it in a thread and return response
        deletionThread = threading.Thread(target=self.deleteRelatedCartItems, args=[currentCartItems])
        deletionThread.start()

        return Response(OrderSerializer.serialize(newOrder), status=201)
        
class OwnOrderSingleOperations(MultipleLookUpFieldMixin, RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = {
        'userId': 'customer__pk',
        'orderId': 'pk'
    }

    def get(self, request, *args, **kwargs):
        self.kwargs['userId'] = request.user.id
        return super().get(request, *args, **kwargs)
