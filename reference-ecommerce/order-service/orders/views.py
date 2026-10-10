from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Order, OrderStatus
from .serializers import OrderSerializer
# Create your views here.

class ListCreateOrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class RetrieveOrderView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReserveInventoryView(APIView):
    def post(self, request: Request, pk):
        order = get_object_or_404(Order, pk=pk)
        try:
            order.transition_to(OrderStatus.INVENTORY_RESERVED)
        except ValueError:
            return Response({
                "detail" : "Invalid order status transiton."
            }, status=status.HTTP_409_CONFLICT)
        return Response({
            "message" : f"The Status of Order {order.id} has been changed to Inventory Reserved",
            "data" : OrderSerializer(order).data
        }, status=status.HTTP_200_OK)



