from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core import mail
from users.models import ContractUser


class NewUserAPITestCase(APITestCase):

    def test_user(self):
        # Test create inactive user and send verification email
        endpoint = reverse("user-list")
        data = {
            "username": "testUser",
            "email": "testUser@company.com",
            "password": "123456",
        }
        response = self.client.post(endpoint, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(mail.outbox), 1)  # test if email is sent

        # Test account verification
        token = mail.outbox[0].body.split("=")[1]
        response = self.client.get(endpoint, data={"token": token}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test verification email resending
        endpoint = reverse("user-resend-email")
        data = {"username": "testUser"}
        response = self.client.post(endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(mail.outbox), 2)  # test if email is sent
