from django.test import TestCase
from .models import ContractUser


class ContractUserTestCase(TestCase):

    def setUp(self):
        self.user = ContractUser.objects.create_user(
            username="user", password="123", email="user@company.com"
        )
        self.superuser = ContractUser.objects.create_superuser(
            username="admin",
            password="123",
            email="admin@company.com",
        )

    def test_create(self):
        self.assertEqual(self.user.username, "user")
        self.assertEqual(self.user.email, "user@company.com")
        self.assertEqual(self.user.profile, "client")
        self.assertEqual(str(self.user), "user")
        self.assertFalse(self.user.is_active)

        with self.assertRaisesMessage(ValueError, "Email field is required"):
            ContractUser.objects.create_user(username="user1", email="", password="123")

    def test_create_superuser(self):
        self.assertTrue(self.superuser.is_superuser)
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_active)
        self.assertEqual(self.superuser.username, "admin")
