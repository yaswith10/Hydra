from django.urls import path

from .views import ListCreateOrderView, RetrieveOrderView, ReserveInventoryView

urlpatterns = [
    path("orders/", ListCreateOrderView.as_view(), name="orders"),
    path("orders/<int:pk>/", RetrieveOrderView.as_view(), name="order"),
    path("orders/<int:pk>/reserve-inventory/", ReserveInventoryView.as_view(), name="reserve-inventory")
]