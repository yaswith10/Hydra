from decimal import Decimal
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "customer", "status", "total_amount", "created_at", "updated_at"]
        read_only_fields = ["id", "status", "created_at", "updated_at"]

    def validate_total_amount(self, value):
        if value <= Decimal("0.00"):
            raise serializers.ValidationError(
                "Order total must be greater than zero."
            )
        return value