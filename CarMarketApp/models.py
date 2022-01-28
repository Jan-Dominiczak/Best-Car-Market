from django.db import models
from django.contrib.auth.models import User

class Dealer(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    seller_status = models.CharField(max_length = 30)       # private/dealer/used car dealer
    username = models.CharField(max_length = 30)

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.city)

class Car(models.Model):
    brand = models.CharField(max_length = 30)
    model = models.CharField(max_length = 30)
    gen = models.CharField(max_length = 30)
    year = models.CharField(max_length = 30)
    status = models.CharField(max_length = 30)              # new/used/damaged
    available = models.BooleanField(max_length = 30)        # True/False
    price = models.FloatField(max_length = 30)
