from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import ContractUser


class ContractUserAPITestCase(APITestCase):

    def test_create(self):
        endpoint = reverse("user-list")
        user_data = {"username": "user", "password": "123", "email": "user@company.com"}
        response = self.client.post(endpoint, data=user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve(self):
        user = ContractUser.objects.create(
            username="user",
            password="123",
            email="user@company.com",
        )
        endpoint = reverse("user-detail", args=[user.id])
        response = self.client.get(endpoint, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
