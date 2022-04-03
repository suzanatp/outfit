from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.db import models

from outfit.accounts.managers import OutfitUserManager


class OutfitUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 15
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    USERNAME_FIELD = 'username'

    objects = OutfitUserManager()
