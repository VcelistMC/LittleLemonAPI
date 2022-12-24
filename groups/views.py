import json
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User, Group
from core.models import LittleLemonUser

from core.models import UserGroups
# Create your views here.


@api_view(['POST', 'GET'])
def users_of_group(request, group):
    currentUser = LittleLemonUser.objects.get(pk=request.user.id)
    if(not currentUser.belongsToGroup(UserGroups.MANAGER)):
        return Response({"detail": "You're not authorized to view this page"}, status=403)

    if request.method == "GET":
        return Response(LittleLemonUser.objects.filter(groups__name=group))

    if request.method == "POST":
        jsonStr = json.loads(request.body.decode('utf-8'))
        userId = jsonStr['userId']
        selectedUser = LittleLemonUser.objects.get(pk=userId)

        requestedGroup = Group.objects.get(name=group)
        requestedGroup.user_set.add(selectedUser)

        return Response({"detail": "User added to group"}, status=201)
