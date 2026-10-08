from rest_framework.serializers import ModelSerializer
from .models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "customer", "status", "total_amount", "created_at", "updated_at"]
        read_only_fields = ["id", "status", "created_at", "updated_at"]
        