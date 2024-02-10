from django.test import TestCase
from users.models import ContractUser
from ...models import Warehouse


class WarehouseTestCase(TestCase):

    def setUp(self):
        self.user = ContractUser.objects.create(
            username="user", password="123", email="user@company.com"
        )
        self.warehouse = Warehouse.objects.create(
            warehouse_name="TestWarehouse",
            warehouse_info="TestWarehouse info",
            client=self.user,
        )

    def test_create(self):
        self.assertEqual(self.warehouse.warehouse_name, "TestWarehouse")
        self.assertEqual(self.warehouse.warehouse_info, "TestWarehouse info")
        self.assertEqual(self.warehouse.client, self.user)
        self.assertEqual(str(self.warehouse), "TestWarehouse")
