from rest_framework.permissions import BasePermission
from .models import LittleLemonUser, UserGroups
from rest_framework import exceptions

class ReadOnlyForNonManager(BasePermission):
    def has_permission(self, request, view):
        if request.user is None: raise exceptions.NotAuthenticated()

        if(request.method == "GET"): return True
        
        currentUser = LittleLemonUser.objects.get(pk=request.user.id)
        return currentUser.belongsToGroup(UserGroups.MANAGER)


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user is None: raise exceptions.NotAuthenticated()

        currentUser = LittleLemonUser.objects.get(pk=request.user.id)
        return currentUser.belongsToGroup(UserGroups.MANAGER) 

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user is None: raise exceptions.NotAuthenticated()

        currentUser = LittleLemonUser.objects.get(pk=request.user.id)
        return currentUser.belongsToGroup(UserGroups.MANAGER) or currentUser.belongsToGroup(UserGroups.DELIVERY_CREW)