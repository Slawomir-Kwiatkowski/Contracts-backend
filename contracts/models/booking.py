from django.db import models
from django.core import validators
from .contract import Contract


class Booking(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    pallets_actual = models.IntegerField(
        validators=(
            validators.MinValueValidator(1),
            validators.MaxValueValidator(30, "Max number of pallets is 30"),
        )
    )
    driver_full_name = models.CharField(max_length=20)
    driver_phone_number = models.CharField(max_length=10)
    truck_reg_number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.contract)
