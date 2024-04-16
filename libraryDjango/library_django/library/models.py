from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=200)
    checked_out = models.BooleanField()
    checkout_date = models.DateField()