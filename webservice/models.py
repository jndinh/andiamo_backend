from django.db import models
import django.utils.timezone as time

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=128)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)

    def __str__(self):
        return "%s" % (self.email)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    street_address = models.CharField(max_length=50, null=False, blank=False)
    line_number = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    state = models.CharField(max_length=2, null=False, blank=False)
    zip_code = models.CharField(max_length=5, null=False, blank=False)

class Store(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Order(models.Model):
    total = models.FloatField()
    timestamp = models.DateTimeField(default=time.now)
