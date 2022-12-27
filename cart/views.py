from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from cart.models import Cart
from cart.serializers import CartSerializer
from core.models import LittleLemonUser
from core.permissions import IsManager
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.


class AllCartsView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsManager]

list_create_cart_view = AllCartsView.as_view()

class OwnCartView(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        currentUser = LittleLemonUser.objects.get(pk=request.user.id)
        currentUserCart = Cart.objects.get_or_create(userId = currentUser)
        return Response(CartSerializer.serialize(currentUserCart))

own_cart_view = OwnCartView.as_view()
