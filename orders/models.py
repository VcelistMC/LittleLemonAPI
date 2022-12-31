from django.db import models

from core.models import LittleLemonUser
from menu.models import MenuItem

# Create your models here.

class OrderStatus(models.TextChoices):
    PENDING =  'PENDING'
    ASSIGNED = 'ASSIGNED'
    DELIVERED = 'DELIVERED'

class Order(models.Model):
    customer = models.ForeignKey(LittleLemonUser, on_delete=models.CASCADE, related_name='customer')
    delivery_crew = models.ForeignKey(LittleLemonUser, on_delete=models.SET_NULL, null=True, related_name='delivery_crew', default=None)
    status = models.CharField(
        max_length=15,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now=True)

    @property
    def orderTotal(self):
        items = OrderItem.objects.select_related('menuItem').filter(order=self.pk)
        total = 0
        for item in items:
            total += item.total

        return total

    def assignToCrew(self, crew: LittleLemonUser):
        self.delivery_crew = crew
        self.status = OrderStatus.ASSIGNED


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    @property
    def total(self):
        return self.menuItem.basePrice * self.quantity

    def __str__(self) -> str:
        return f'{self.quantity}x {self.menuItem}'