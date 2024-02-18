from django.db import models
from users.models import ContractUser
from .contract import Contract


class Booking(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    pallets_actual = models.IntegerField()
    driver_full_name = models.CharField(max_length=20)
    driver_phone_number = models.CharField(max_length=10)
    truck_reg_number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.contract)
