from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# class Dealer(models.Model):
#     first_name = models.CharField(max_length = 30)
#     last_name = models.CharField(max_length = 30)
#     city = models.CharField(max_length = 30)
#     seller_status = models.CharField(max_length = 30)       # private/dealer/used car dealer


#     def __str__(self):
#         return "%s %s %s" % (self.first_name, self.last_name, self.city)

class Car(models.Model):
    col1 = models.AutoField(primary_key=True)
    brand = models.CharField(max_length = 30)
    model = models.CharField(max_length = 30)
    gen = models.CharField(max_length = 30)
    year = models.CharField(max_length = 30)
    status = models.CharField(max_length = 32, choices =[('new', 'New'), ('used', 'Used'), ('damaged', 'Damaged')])              # new/used/damaged
    available = models.BooleanField(max_length = 30)        # True/False
    price = models.FloatField(max_length = 30)
    description = models.TextField(max_length = 4000, default='')
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Seller") 
    # {self.seller_id.first_name} {self.seller_id.last_name}

    def __str__(self):
        return f"{self.brand}, {self.model}, {self.gen}, {self.year}, {self.status}, {self.available}, {self.price}, {self.seller_id.first_name} {str(self.seller_id.last_name)[0]}."

    def get_absolute_url_edit(self):
        return reverse('edit_post', kwargs={"pk": self.pk})

    def get_absolute_url_details(self):
        return reverse('details', kwargs={"pk": self.pk})