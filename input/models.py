from django.db import models
from django import forms
# Create your models here.
class CostOfGood(models.Model):
    item_no = models.CharField(max_length= 200)
    part_no = models.TextField()
    product_description = models.TextField()
    unitMarketPrice = models.FloatField()
    quantity = models.FloatField()
    markup = models.FloatField()

class ConstantField(models.Model):
    freightAndInsurance = models.FloatField()
    otherCosts = models.FloatField()
    customsRate = models.FloatField()
    exciseTax = models.FloatField()
    vat = models.FloatField()
    surtax = models.FloatField()
    withholdingTax = models.FloatField()

class User(models.Model):
    username =  models.CharField(max_length=100, default="user")
    password = models.CharField(max_length= 100)

    def __str__(self):
        return self.username
      