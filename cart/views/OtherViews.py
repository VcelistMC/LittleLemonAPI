from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer, CartSerializer, CartItemPostRequestSerializer
from core.mixins import MultipleLookUpFieldMixin
from core.permissions import IsManager
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination


class AllCartsView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsManager]
    pagination_class = LimitOffsetPagination


class CartSingleOPsView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsManager]


class CartItemsView(ListCreateAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [IsManager]
    serializer_class = CartItemSerializer
    pagination_class = LimitOffsetPagination

    def post(self, request, *args, **kwargs):
        dto = CartItemPostRequestSerializer(data= request.data)

        if not dto.is_valid():
            return Response(dto.errors, status=400)
        
        cart = get_object_or_404(Cart, pk=kwargs['cartId'])

        createdItem = dto.save(cart.user.pk)

        return Response({CartItemSerializer.serialize(createdItem)}, status=201)


class CartItemsSingleOpsView(MultipleLookUpFieldMixin, RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [IsManager]
    serializer_class = CartItemSerializer
    lookup_fields = {'itemId': 'pk', 'cartId': 'cart__pk'}

