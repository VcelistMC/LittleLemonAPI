from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer, CartSerializer, CartItemPostRequestSerializer
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

class OwnCartView(APIView):
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        currentUserCart, _ = Cart.objects.get_or_create(user__pk = request.user.id)
        return Response(CartSerializer.serialize(currentUserCart))

own_cart_view = OwnCartView.as_view()


class OwnCartItemsView(APIView):
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cartItems = CartItem.objects.filter(cart__user=request.user.id)
        seri = CartItemSerializer(cartItems, many=True)
        return Response(seri.data)

    def post(self, request, *args, **kwargs):
        dto = CartItemPostRequestSerializer(data= request.data)
        if not dto.is_valid():
            return Response(dto.errors, status=400)
        
        dto.save(request.user.id)

        return Response({"done": "bibi"})

own_cart_items_view = OwnCartItemsView.as_view()


class OwnCartItemSingleOpsView(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

own_cart_item_single_ops_view = OwnCartItemSingleOpsView.as_view()

