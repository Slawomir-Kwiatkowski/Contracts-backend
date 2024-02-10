from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .warehouse import Warehouse


class Contract(models.Model):
    pass

    # class Meta:
    #     ordering = ("-date_of_order",)

    # class StatusChoices(models.TextChoices):
    #     OPEN = "OPEN"
    #     ACCEPTED = "accepted"
    #     CANCELLED = "cancelled"

    # status = models.CharField(
    #     max_length=10, choices=StatusChoices, default=StatusChoices.OPEN
    # )
    # contract_number = models.CharField(max_length=15)
    # client = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_of_order = models.DateField(default=timezone.now)
    # date_of_delivery = models.DateField()
    # time_of_delivery = models.TimeField()
    # pallets_planned = models.IntegerField()
    # Warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.contract_number
