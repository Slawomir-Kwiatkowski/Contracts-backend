from django.db import models
from django.core import validators
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

    class DeliveryDateValidator:
        def validate(value):
            if value < timezone.now().date():
                raise validators.ValidationError(
                    "Date of delivery can't be earlier than date of order"
                )
            else:
                return value

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
    date_of_delivery = models.DateField(validators=(DeliveryDateValidator.validate,))
    time_of_delivery = models.TimeField()
    pallets_planned = models.IntegerField(
        validators=(
            validators.MinValueValidator(1),
            validators.MaxValueValidator(30, "Max number of pallets is 30"),
        )
    )
    # warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    warehouse = models.CharField(choices=warehouses_choices, max_length=15)
    #

    def __str__(self):
        return self.contract_number
