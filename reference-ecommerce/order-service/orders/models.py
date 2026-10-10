from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class OrderStatus(models.TextChoices):
    PENDING = ("PENDING", "Pending")
    INVENTORY_RESERVED = ("INVENTORY_RESERVED", "Inventory Reserved")
    PAYMENT_COMPLETED = ("PAYMENT_COMPLETED", "Payment Completed")
    COMPLETED = ("COMPLETED", "Completed")

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20, 
        choices=OrderStatus, 
        default=OrderStatus.PENDING
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ALLOWED_TRANSITIONS = {
        OrderStatus.PENDING : { OrderStatus.INVENTORY_RESERVED},
        OrderStatus.INVENTORY_RESERVED : { OrderStatus.PAYMENT_COMPLETED},
        OrderStatus.PAYMENT_COMPLETED: {OrderStatus.COMPLETED}
    }

    def transition_to(self, new_status):
        allowed = self.ALLOWED_TRANSITIONS.get(self.status, set())

        if new_status not in allowed:
            raise ValueError(
                f"Invalid order status transition: {self.status} -> {new_status}"
            )

        self.status = new_status
        self.save(update_fields=["status", "updated_at"])

    