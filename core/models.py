from django.db import models
from datetime import date

from django.core.validators import MinValueValidator

# Create your models here.

class Customer(models.Model):
    account = models.OneToOneField("accounts.Account", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    birthday = models.DateField(null=True, validators=[
        MinValueValidator(date(2000, 1, 1), 'Must be born in 2001-01')
    ])

    def __str__(self):
        return f"Person born on {self.date_of_birth}"