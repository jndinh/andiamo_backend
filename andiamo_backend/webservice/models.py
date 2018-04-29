from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
