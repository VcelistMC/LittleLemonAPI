from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from core.models import UserGroups
from core.permissions import IsStaff
from rest_framework.response import Response
from rest_framework import exceptions

from orders.models import Order
from orders.serializers import OrderDeliveryPatchRequest, OrderManagerPatchRequest, OrderSerializer


class AllOrdersView(APIView):
    permission_classes = [IsStaff]

    def get(self, request, *args, **kwargs):
        currentUser = request.user

        if currentUser.belongsToGroup(UserGroups.MANAGER):
            return self.getAllOrders(request, args, kwargs)
        elif currentUser.belongsToGroup(UserGroups.DELIVERY_CREW):
            return self.getAssignedOrders(request, args, kwargs)

    def getAllOrders(self, request, *args, **kwargs):
        allOrders = Order.objects.all()
        return Response(OrderSerializer.serialize(allOrders, True))

    def getAssignedOrders(self, request, *args, **kwargs):
        allAssignedOrders = Order.objects.filter(delivery_crew__pk = request.user.id)
        return Response(OrderSerializer.serialize(allAssignedOrders, True))


class OrdersSingleOpsView(APIView):
    permission_classes = [IsStaff]

    def get(self, request, *args, **kwargs):
        currentUser = request.user

        if currentUser.belongsToGroup(UserGroups.MANAGER):
            return self.getOrder(request, *args, **kwargs)
        elif currentUser.belongsToGroup(UserGroups.DELIVERY_CREW):
            return self.getOrderIfAssigned(request, *args, **kwargs)

    
    def getOrder(self, request, *args, **kwargs):
        orderId = kwargs['orderId']
        order = get_object_or_404(Order, pk=orderId)

        return Response(OrderSerializer.serialize(order))

    def getOrderIfAssigned(self, request, *args, **kwargs):
        orderId = kwargs['orderId']

        order = get_object_or_404(Order, pk=orderId, delivery_crew__pk=request.user.id)

        return Response(OrderSerializer.serialize(order))

    
    def patch(self, request, *args, **kwargs):
        currentUser = request.user

        if currentUser.belongsToGroup(UserGroups.MANAGER):
            return self.patchOrder(request, *args, **kwargs)
        elif currentUser.belongsToGroup(UserGroups.DELIVERY_CREW):
            return self.patchOrderIfAssinged(request, *args, **kwargs)

    def patchOrder(self, request, *args, **kwargs):
        orderId = kwargs['orderId']
        order = get_object_or_404(Order, pk=orderId)


        bodySerializer = OrderManagerPatchRequest(data=request.data)

        if not bodySerializer.is_valid():
            return Response(bodySerializer.errors, status=400)

        patchedOrder = bodySerializer.save(order)

        return Response(OrderSerializer.serialize(patchedOrder))

    def patchOrderIfAssinged(self, request, *args, **kwargs):
        orderId = kwargs['orderId']
        order = get_object_or_404(Order, pk=orderId, delivery_crew__pk=request.user.id)


        bodySerializer = OrderDeliveryPatchRequest(data=request.data)

        if not bodySerializer.is_valid():
            return Response(bodySerializer.errors, status=400)

        patchedOrder = bodySerializer.save(order)

        return Response(OrderSerializer.serialize(patchedOrder))

    
    def delete(self, request, *args, **kwargs):
        currentUser = request.user
        if not currentUser.belongsToGroup(UserGroups.MANAGER):
            raise exceptions.PermissionDenied()
        
        orderId = kwargs['orderId']
        order = get_object_or_404(Order, pk=orderId)
        order.delete()

        return Response({"detail": "Deleted"})

