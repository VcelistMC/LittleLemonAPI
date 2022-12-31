from rest_framework.views import APIView
from core.models import UserGroups
from core.permissions import IsStaff
from rest_framework.response import Response


class AllOrdersView(APIView):
    permission_classes = [IsStaff]

    def get(self, request, *args, **kwargs):
        currentUser = request.user

        if currentUser.belongsToGroup(UserGroups.MANAGER):
            return Response({"role": "manager"})
        elif currentUser.belongsToGroup(UserGroups.DELIVERY_CREW):
            return Response({"role": "Deliveryy"})

        return Response({"role": "You shouldn't be able to see this"})