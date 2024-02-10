from django.test import TestCase
from .models import ContractUser


class ContractUserTestCase(TestCase):

    def setUp(self):
        self.user = ContractUser.objects.create(
            username="user", password="123", email="user@company.com"
        )

    def test_create(self):
        self.assertEqual(self.user.username, "user")
        self.assertEqual(self.user.email, "user@company.com")
        self.assertEqual(self.user.profile, "client")
        self.assertEqual(str(self.user), "user")
