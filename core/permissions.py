from rest_framework.permissions import BasePermission
from .models import LittleLemonUser, UserGroups

class ReadOnlyForNonManager(BasePermission):
    def has_permission(self, request, view):
        if(request.method == "GET"): return True
        
        currentUser = LittleLemonUser.objects.get(pk=request.user.id)
        return currentUser.belongsToGroup(UserGroups.MANAGER)


class IsManager(BasePermission):
    def has_permission(self, request, view):
        currentUser = LittleLemonUser.objects.get(pk=request.user.id)
        return currentUser.belongsToGroup(UserGroups.MANAGER) 