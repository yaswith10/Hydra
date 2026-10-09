from django.urls import path

from .views import ListCreateOrderView, RetrieveOrderView

urlpatterns = [
    path("orders/", ListCreateOrderView.as_view(), name="orders"),
    path("orders/<int:pk>/", RetrieveOrderView.as_view(), name="order")
]