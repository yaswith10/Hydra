from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import Order, OrderStatus

# Create your tests here.

class OrderAPITests(APITestCase):

    def setUp(self):
        self.customer = User.objects.create_user(
            username="test-customer",
            password="Test@123"
        )
    
    def test_create_order(self):
        response = self.client.post(
            "/orders/api/orders/",
            {
                "customer" : self.customer.id,
                "total_amount" : "100.00"
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(response.data["status"], "PENDING")

    def test_negative_amount(self):
        response = self.client.post(
            "/orders/api/orders/",
            {
                "customer" : self.customer.id,
                "total_amount" : "-100.00"
            },
            format="json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Order.objects.count(), 0)

    def test_missing_amount(self):
        response = self.client.post(
            "/orders/api/orders/",
            {
                "customer": self.customer.id,
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Order.objects.count(), 0)
    
    def test_fetch_correct_order(self):
        order = Order.objects.create(
            customer = self.customer,
            total_amount = "100.00"
        )
        response = self.client.get(
            f"/orders/api/orders/{order.id}/",
            format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_fetch_wrong_order(self):
        response = self.client.get(
            f"/orders/api/orders/{999}/",
            format="json"
        )
        self.assertEqual(response.status_code, 404)

    def test_valid_transition(self):
        order = Order.objects.create(customer=self.customer, total_amount="100.00")
        order.transition_to(OrderStatus.INVENTORY_RESERVED)
        order.refresh_from_db()
        self.assertEqual(order.status, OrderStatus.INVENTORY_RESERVED)

    def test_invalid_transition(self):
        order = Order.objects.create(customer=self.customer, total_amount="100.00")
        with self.assertRaises(ValueError):
            order.transition_to(OrderStatus.PAYMENT_COMPLETED)
        order.refresh_from_db()
            

