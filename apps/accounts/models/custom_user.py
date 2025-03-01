from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserModel(AbstractUser):
    # ROLES = [
    #     ("admin", "Admin"),
    #     ("moderator", "Moderator"),
    #     ("customer", "Customer"),
    # ]
    # role = models.CharField(max_length=20, choices=ROLES, default="customer")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"

    @property
    def role(self):
        if self.is_superuser:
            return "admin"
        elif self.is_staff:
            return "moderator"
        else:
            return "customer"
