from django.db import models
from django.utils import timezone
from users.models import ContractUser
from .warehouse import Warehouse


class Contract(models.Model):

    class Meta:
        ordering = ("-date_of_order",)

    class StatusChoices(models.TextChoices):
        OPEN = "open"
        ACCEPTED = "accepted"
        CANCELLED = "cancelled"

    status = models.CharField(
        max_length=10, choices=StatusChoices, default=StatusChoices.OPEN
    )
    contract_number = models.CharField(max_length=15)
    client = models.ForeignKey(ContractUser, on_delete=models.CASCADE)
    contractor = models.ForeignKey(
        ContractUser, on_delete=models.PROTECT, related_name="+"
    )
    date_of_order = models.DateField(default=timezone.now)
    date_of_delivery = models.DateField()
    time_of_delivery = models.TimeField()
    pallets_planned = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)

    def __str__(self):
        return self.contract_number
