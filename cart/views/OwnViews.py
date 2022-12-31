from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer, CartSerializer, CartItemPostRequestSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from core.mixins import MultipleLookUpFieldMixin

class OwnCartView(APIView):
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        currentUserCart, _ = Cart.objects.get_or_create(user__pk = request.user.id)
        return Response(CartSerializer.serialize(currentUserCart))



class OwnCartItemsView(APIView):
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        cartItems = CartItem.objects.filter(cart__user=request.user.id)
        return Response(CartItemSerializer.serialize(cartItems, many=True))

    def post(self, request, *args, **kwargs):
        dto = CartItemPostRequestSerializer(data= request.data)
        if not dto.is_valid():
            return Response(dto.errors, status=400)
        
        createdItem = dto.save(request.user.id)

        return Response(CartItemSerializer.serialize(createdItem), status=201)



class OwnCartItemSingleOpsView(MultipleLookUpFieldMixin,  RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = {'userId': 'cart__user__pk', 'pk': 'pk'}

    def get_object(self):
        self.kwargs['userId'] = self.request.user.id
        return super().get_object()
