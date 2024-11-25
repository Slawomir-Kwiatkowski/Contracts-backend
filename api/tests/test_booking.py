from rest_framework.test import APITestCase
from rest_framework import status
from datetime import timedelta, datetime
from django.utils import timezone
from django.urls import reverse
from users.models import ContractUser
from contracts.models import Booking, Warehouse, Contract


class BookingAPITestCase(APITestCase):

    def setUp(self):

        self.client1 = ContractUser.objects.create(
            username="client1", password="123", email="client1@company.com"
        )

        self.contractor1 = ContractUser.objects.create(
            username="contractor1",
            password="123",
            email="contractor1@company.com",
            profile="contractor",
        )

        self.warehouse = Warehouse.objects.create(
            warehouse_name="Warehouse",
            warehouse_info="Warehouse info",
            client=self.client1,
        )

        self.contract = Contract.objects.create(
            contract_number="A01",
            client=self.client1,
            contractor=self.contractor1,
            date_of_delivery=timezone.now() + timedelta(1),
            time_of_delivery="12:00",
            pallets_planned=1,
            warehouse=self.warehouse,
        )

        self.booking = Booking.objects.create(
            contract=self.contract,
            pallets_actual=1,
            driver_full_name="John Doe",
            driver_phone_number="555 555 55",
            truck_reg_number="AAA 12345",
        )

        self.client.force_authenticate(user=self.contractor1)

    def test_get(self):
        endpoint = reverse("booking-list")
        response = self.client.get(endpoint, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        Booking.objects.get(id=1).delete()
        endpoint = reverse("booking-list")
        data = {
            "contract": self.contract.id,
            "pallets_actual": 1,
            "driver_full_name": "John Doe",
            "driver_phone_number": "555 555 55",
            "truck_reg_number": "AAA 12345",
        }
        response = self.client.post(endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve(self):
        endpoint = reverse("booking-detail", args=[self.booking.id])
        response = self.client.get(endpoint, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["contract"], 1)

    def test_update(self):
        data = {
            "pallets_actual": 2,
        }
        endpoint = reverse("booking-detail", args=[self.booking.id])
        response = self.client.patch(endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["pallets_actual"], 2)

    def test_delete(self):
        endpoint = reverse("booking-detail", args=[self.booking.id])
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
