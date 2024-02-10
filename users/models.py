from django.db import models
from django.contrib.auth.models import AbstractUser


class ContractUser(AbstractUser):

    class ProfileChoices(models.TextChoices):
        CLIENT = "client"
        CONTRACTOR = "contractor"

    profile = models.TextField(
        choices=ProfileChoices.choices, default=ProfileChoices.CLIENT
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.username
