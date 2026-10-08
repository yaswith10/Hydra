from rest_framework.generics import ListCreateAPIView
from .models import Order
from .serializers import OrderSerializer
# Create your views here.

class ListCreateOrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
