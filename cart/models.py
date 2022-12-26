from django.db import models
from menu.models import MenuItem
from core.models import LittleLemonUser

class Cart(models.Model):
    userId = models.ForeignKey(LittleLemonUser, on_delete=models.CASCADE)

    @property
    def cartTotal(self):
        items = CartItem.objects.filter(cart=self.pk)
        total = 0
        for item in items:
            total += item.total

        return total

    def __str__(self) -> str:
        return self.userId.username + "'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart")
    menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def total(self):
        return self.menuItem.basePrice * self.quantity

    def __str__(self) -> str:
        return f'{self.quantity}x {self.menuItem}'
