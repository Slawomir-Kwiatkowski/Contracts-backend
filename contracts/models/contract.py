from django.db import models
from django.core import validators
from django.utils import timezone
from users.models import ContractUser
from .warehouse import Warehouse


class Contract(models.Model):

    class Meta:
        ordering = ("-date_of_order",)

    class DeliveryDateValidator:
        def validate(value):
            if value < timezone.now().date():
                raise validators.ValidationError(
                    "Date of delivery can't be earlier than date of order"
                )
            else:
                return value

    status = models.CharField(max_length=9, default="open")
    contract_number = models.CharField(max_length=15, unique=True)
    client = models.ForeignKey(ContractUser, on_delete=models.CASCADE)
    contractor = models.ForeignKey(
        ContractUser, on_delete=models.CASCADE, related_name="+"
    )
    date_of_order = models.DateTimeField(default=timezone.now)
    date_of_delivery = models.DateField(validators=(DeliveryDateValidator.validate,))
    time_of_delivery = models.TimeField()
    pallets_planned = models.IntegerField(
        validators=(
            validators.MinValueValidator(1),
            validators.MaxValueValidator(30, "Max number of pallets is 30"),
        )
    )
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.contract_number
