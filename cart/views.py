from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from cart.models import Cart, CartItem
from cart.serializers import CartItemPostRequestSerializer, CartItemSerializer, CartSerializer
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


class OwnCartItemsView(ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemPostRequestSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        cartItems = CartItem.objects.filter(cart__userId=request.user.id)
        seri = CartItemSerializer(cartItems, many=True)
        return Response(seri.data)

    def post(self, request, *args, **kwargs):
        s = CartItemPostRequestSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        s.save()
        print(s.validated_data)
own_cart_items_view = OwnCartItemsView.as_view()