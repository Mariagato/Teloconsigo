from email.policy import default
from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length= 100)
    identification = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    phone_Number = models.CharField(max_length= 100)
    email = models.CharField(max_length= 100)


    def __str__(self):
        return f'{self.name} {self.identification} {self.address} {self.phone_Number} {self.email}'

# Create your models here.
