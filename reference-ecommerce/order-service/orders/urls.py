from django.urls import path

from .views import ListCreateOrderView, RetriveUpdateDestroyOrderView

urlpatterns = [
    path("orders/", ListCreateOrderView.as_view(), name="orders"),
    path("orders/<int:pk>/", RetriveUpdateDestroyOrderView.as_view(), name="order")
]