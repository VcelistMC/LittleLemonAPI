import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import Group
from core.models import LittleLemonUser
from core.serializers import LittleLemonUserSerializer
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from core.permissions import ReadOnlyForNonManager

from core.models import UserGroups


class GetCreateUserGroups(ListCreateAPIView, DestroyAPIView):
    queryset = LittleLemonUser
    serializer_class = LittleLemonUserSerializer
    permission_classes = [IsAuthenticated, ReadOnlyForNonManager]

    def list(self, request, *args, **kwargs):
        group = kwargs['group']
        usersInGroup = LittleLemonUser.objects.filter(groups__name=group)
        return Response(LittleLemonUserSerializer.serialize(usersInGroup, True))

    def post(self, request, *args, **kwargs):
        group = kwargs['group']
        userId = request.data['userId']
        selectedUser = LittleLemonUser.objects.get(pk=userId)
        if(selectedUser == None):
            return Response({"detail": f'{userId} not found'}, status=400)

        requestedGroup = Group.objects.get(name=group)
        if(requestedGroup == None):
            return Response({"detail": f'{group} not found'}, status=400)

        requestedGroup.user_set.add(selectedUser)

        return Response({"detail": f'{selectedUser.username} added to {group}'}, status=201)


class DeleteUserFromGroup(DestroyAPIView):
    queryset = LittleLemonUser
    serializer_class = LittleLemonUserSerializer
    permission_classes = [IsAuthenticated, ReadOnlyForNonManager]

    def destroy(self, request, *args, **kwargs):
        userIdToDelete = kwargs['userId']
        groupNameToDeleteFrom = kwargs['group']

        groupToDeleteFrom = Group.objects.get(name = groupNameToDeleteFrom)
        userToDelete = LittleLemonUser.objects.get(pk=userIdToDelete)

        if(userToDelete == None):
            return Response({"detail": "user not found"}, status=400)

        groupToDeleteFrom.user_set.remove(userToDelete)

        return Response({"detail": f'{userToDelete.username} removed from {groupNameToDeleteFrom}'}, status=200)