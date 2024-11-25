from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import ContractUser
from contracts.models import Warehouse


class WarehouseAPITestCase(APITestCase):

    def setUp(self):
        self.user = ContractUser.objects.create(
            username="TestUser", password="123", email="testuser@company.com"
        )
        self.warehouse = Warehouse.objects.create(
            warehouse_name="Warehouse",
            warehouse_info="Warehouse info",
            client=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_get(self):
        endpoint = reverse("warehouse-list")
        response = self.client.get(endpoint, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        endpoint = reverse("warehouse-list")
        data = {
            "warehouse_name": "Warehouse-new",
            "warehouse_info": "Warehouse-new info",
            "client": self.user.id,
        }
        response = self.client.post(endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve(self):
        endpoint = reverse("warehouse-detail", args=[self.warehouse.id])
        response = self.client.get(endpoint, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["warehouse_name"], "Warehouse")

    def test_update(self):
        data = {
            "warehouse_name": "Warehouse-upd",
            "warehouse_info": "Warehouse1-upd info",
            "client": self.user.id,
        }
        endpoint = reverse("warehouse-detail", args=[self.warehouse.id])
        response = self.client.put(endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["warehouse_name"], "Warehouse-upd")

    def test_delete(self):
        endpoint = reverse("warehouse-detail", args=[self.warehouse.id])
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
