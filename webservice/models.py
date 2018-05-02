from django.db import models
import django.utils.timezone as time

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)

class Store(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Order(models.Model):
    total = models.FloatField()
    timestamp = models.DateTimeField(default=time.now)
