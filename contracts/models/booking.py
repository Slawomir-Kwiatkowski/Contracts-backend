from django.db import models
from django.contrib.auth.models import User
from .contract import Contract


class Booking(models.Model):
    pass
    # contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    # contractor = models.ForeignKey(User, on_delete=models.CASCADE)
    # pallets_actual = models.IntegerField()
    # driver_full_name = models.CharField(max_length=20)
    # driver_phone_number = models.CharField(max_length=10)
    # truck_reg_number = models.CharField(max_length=10)
