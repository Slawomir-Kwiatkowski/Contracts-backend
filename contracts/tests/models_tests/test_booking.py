from django.test import TestCase
from users.models import ContractUser
from ...models import Warehouse, Contract, Booking


class BookingTestCase(TestCase):

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
        self.contract = Contract.objects.create(
            contract_number="AAA12345",
            client=self.client,
            contractor=self.contractor,
            date_of_delivery="2024-01-01",
            time_of_delivery="12:00",
            warehouse=self.warehouse,
            pallets_planned=10,
        )

    def test_create(self):
        booking = Booking.objects.create(
            contract=self.contract,
            pallets_actual=10,
            driver_full_name="John Doe",
            driver_phone_number="555 55 55",
            truck_reg_number="ABC0123",
        )
        self.assertEqual(booking.contract, self.contract)
        self.assertEqual(booking.pallets_actual, 10)
        self.assertEqual(booking.driver_full_name, "John Doe")
        self.assertEqual(booking.driver_phone_number, "555 55 55")
        self.assertEqual(booking.truck_reg_number, "ABC0123")
        self.assertEqual(str(booking), self.contract.contract_number)
