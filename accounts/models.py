from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser): 

    TYPES = (
        (1, "Customer"),
        (2, "Owner"),
    )

    user_type = models.IntegerField(choices=TYPES, default=1)


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='account_user_set',  # unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='account_user_permission_set',  # unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )