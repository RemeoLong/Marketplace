from django.db import models
from django.conf import settings
from django.utils import timezone


class Customer(models.Model):
    customerID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   unique=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30)
    streetAddress = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipCode = models.CharField(max_length=5)
    phoneNumber = models.CharField(max_length=9)

    def publish(self):
        self.creation_date = timezone.now()
        self.save()

    def __str__(self):
        return self.customerID
