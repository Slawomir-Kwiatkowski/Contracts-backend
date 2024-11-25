from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta, datetime
from users.models import ContractUser
from contracts.models import Warehouse, Contract


class ContractAPITestCase(APITestCase):

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
        self.contractor2 = ContractUser.objects.create(
            username="contractor2",
            password="123",
            email="contractor2@company.com",
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
        self.client.force_authenticate(user=self.client1)

    def test_get(self):
        endpoint = reverse("contract-list")
        response = self.client.get(endpoint, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_is_authenticated(self):
        self.client.force_authenticate(user=None)
        endpoint = reverse("contract-list")
        response = self.client.get(endpoint, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data["detail"], "Authentication credentials were not provided."
        )

    def test_create(self):
        endpoint = reverse("contract-list")
        data = {
            "contract_number": "A02",
            "contractor": self.contractor1.id,
            "date_of_delivery": (timezone.now() + timedelta(1)).strftime("%Y-%m-%d"),
            "time_of_delivery": "12:00",
            "pallets_planned": 1,
            "warehouse": self.warehouse.id,
        }
        response = self.client.post(endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_profile_is_client(self):
        self.client.force_authenticate(user=self.contractor1)
        endpoint = reverse("contract-list")
        data = {
            "contract_number": "A02",
            "contractor": self.contractor2.id,
            "date_of_delivery": (timezone.now() + timedelta(1)).strftime("%Y-%m-%d"),
            "time_of_delivery": "12:00",
            "pallets_planned": 1,
            "warehouse": self.warehouse.id,
        }
        response = self.client.post(endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data["detail"], "No sufficient permissions")

    def test_date_of_delivery_validator(self):
        endpoint = reverse("contract-list")
        data = {
            "contract_number": "A02",
            "contractor": self.contractor1.id,
            "date_of_delivery": (timezone.now() - timedelta(1)).strftime("%Y-%m-%d"),
            "time_of_delivery": "12:00",
            "pallets_planned": 1,
            "warehouse": self.warehouse.id,
        }
        response = self.client.post(endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["date_of_delivery"][0],
            "Date of delivery can't be earlier than date of order",
        )

    def test_retrieve(self):
        endpoint = reverse("contract-detail", args=[self.contract.id])
        response = self.client.get(endpoint, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["contract_number"], self.contract.contract_number
        )

    def test_update(self):
        data = {
            "contract_number": "A02",
        }
        endpoint = reverse("contract-detail", args=[self.contract.id])
        response = self.client.patch(endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["contract_number"], "A02")

    def test_delete(self):
        endpoint = reverse("contract-detail", args=[self.contract.id])
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "Contract succesfully cancelled")
