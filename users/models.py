from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import ContractUserManager


class ContractUser(AbstractUser):

    class ProfileChoices(models.TextChoices):
        CLIENT = "client"
        CONTRACTOR = "contractor"

    profile = models.TextField(
        choices=ProfileChoices.choices, default=ProfileChoices.CLIENT
    )
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)

    objects = ContractUserManager()

    def __str__(self):
        return self.username
