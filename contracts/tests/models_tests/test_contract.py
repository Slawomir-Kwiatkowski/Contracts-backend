from django.test import TestCase
from users.models import ContractUser
from ...models import Warehouse, Contract


class WarehouseTestCase(TestCase):

    def setUp(self):
        self.client = ContractUser.objects.create(
            username="client", password="123", email="client@company.com"
        )
        self.contractor = ContractUser.objects.create(
            username="contractor",
            password="123",
            email="user@company.com",
            profile="contractor",
        )
        self.warehouse = Warehouse.objects.create(
            warehouse_name="TestWarehouse",
            warehouse_info="TestWarehouse info",
            client=self.client,
        )

    def test_create(self):
        contract = Contract.objects.create(
            contract_number="AAA12345",
            client=self.client,
            contractor=self.contractor,
            date_of_delivery="2024-01-01",
            time_of_delivery="12:00",
            warehouse=self.warehouse,
            pallets_planned=10,
        )
        self.assertEqual(contract.status, "open")
        self.assertEqual(contract.contract_number, "AAA12345")
        self.assertEqual(str(contract.client), "client")
        self.assertEqual(str(contract.contractor), "contractor")
        self.assertEqual(contract.date_of_delivery, "2024-01-01")
        self.assertEqual(contract.time_of_delivery, "12:00")
        self.assertEqual(str(contract.warehouse), "TestWarehouse")
        self.assertEqual(contract.pallets_planned, 10)
        self.assertEqual(str(contract), "AAA12345")
