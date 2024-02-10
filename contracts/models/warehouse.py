from django.db import models
from users.models import ContractUser


class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=10, unique=True)
    warehouse_info = models.TextField(max_length=100)
    client = models.ForeignKey(ContractUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.warehouse_name
