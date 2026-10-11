from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import logging

from .models import Order, OrderStatus
from .serializers import OrderSerializer

# Create your views here.

logger = logging.getLogger(__name__)


class ListCreateOrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        logger.info("Order created succesfully: order_id=%s", order.pk)

class RetrieveOrderView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReserveInventoryView(APIView):
    def post(self, request: Request, pk):
        order = get_object_or_404(Order, pk=pk)
        try:
            order.transition_to(OrderStatus.INVENTORY_RESERVED)
        except ValueError:
            logger.warning(f"Invalid order status transition", extra={
                "order_id" : order.pk
            })
            return Response({
                "error" : "Invalid order status transition"
            }, status=status.HTTP_409_CONFLICT)
        return Response({
            "message" : f"The status of order {order.id} has been changed to Inventory Reserved",
            "data" : OrderSerializer(order).data
        }, status=status.HTTP_200_OK)

class CompletePaymentView(APIView):
    def post(self, request: Request, pk):
        order = get_object_or_404(Order, pk=pk)
        try:
            order.transition_to(OrderStatus.PAYMENT_COMPLETED)
        except ValueError:
            logger.warning(f"Invalid order status transition", extra={
                "order_id" : order.pk
            })
            return Response({
                "error" : "Invalid order status transition"
            },status=status.HTTP_409_CONFLICT)

        return Response({
            "message" : f"The status of order {order.id} has been changed to Payment Completed",
            "data" : OrderSerializer(order).data
        },status=status.HTTP_200_OK)

class CompleteOrderView(APIView):
    def post(self, request: Request, pk):
        order = get_object_or_404(Order, pk=pk)
        try:
            order.transition_to(OrderStatus.COMPLETED)
        except ValueError:
            logger.warning(f"Invalid order status transition", extra={
                "order_id" : order.pk
            })
            return Response({
                "error" : "Invalid order status transition"
            }, status=status.HTTP_409_CONFLICT)

        return Response({
            "message" : f"The status of order {order.id} has been changed to Completed",
            "data" : OrderSerializer(order).data
        })



