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

    def contractors_choices():
        contractors = ContractUser.objects.filter(profile="contractor").all()
        return [(item.username, item.username) for item in contractors]

    def warehouses_choices():
        warehouses = Warehouse.objects.all()
        return [(item.warehouse_name, item.warehouse_name) for item in warehouses]

    status = models.CharField(
        max_length=10, choices=StatusChoices, default=StatusChoices.OPEN
    )
    contract_number = models.CharField(max_length=15, unique=True)
    client = models.ForeignKey(ContractUser, on_delete=models.CASCADE)
    contractor = models.CharField(choices=contractors_choices, max_length=15)
    # contractor = models.ForeignKey(
    # ContractUser, on_delete=models.PROTECT, related_name="+"
    # )
    date_of_order = models.DateTimeField(default=timezone.now)
    date_of_delivery = models.DateField()
    time_of_delivery = models.TimeField()
    pallets_planned = models.IntegerField()
    # warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    warehouse = models.CharField(choices=warehouses_choices, max_length=15)
    #

    def __str__(self):
        return self.contract_number
