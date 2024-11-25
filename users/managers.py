from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _


class ContractUserManager(UserManager):

    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email field is required"))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        user = self.create_user(username, email, password, **extra_fields)
        return user
