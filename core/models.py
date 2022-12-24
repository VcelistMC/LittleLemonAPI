from django.db import models
from django.contrib.auth.models import AbstractUser


class LittleLemonUser(AbstractUser):
    def belongsToGroup(self, group: str) -> bool:
        return self.groups.filter(name=group).first() != None

class UserGroups:
    MANAGER = "manager"
    DELIVERY_CREW = "delivery-crew"