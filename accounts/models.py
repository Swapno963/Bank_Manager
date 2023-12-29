from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from .constants import ACCOUNT_TYPE, GENDER_TYPE

class UserBank(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete = models.CASCADE)
    account_type = models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null = True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    inital_deposit_date = models.DateField(auto_now_add =True) # User jokhn account create korbe tokhn aita add hoea jabe
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2) # initially balance tahke 0 and 12 degit porjonto rakte parbe and . ar por 2 gor thakbe

    def __str__(self) -> str:
        return self.account_no
    

class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.user.email