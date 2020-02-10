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
    exchange_rate = models.FloatField(default = 0)

class ConstantField(models.Model):
    freightAndInsurance = models.FloatField()
    otherCosts = models.FloatField()
    customsRate = models.FloatField()
    exciseTax = models.FloatField()
    vat = models.FloatField()
    surtax = models.FloatField()
    withholdingTax = models.FloatField()

    def __str__(self):
        return "Constants"

class User(models.Model):
    username =  models.CharField(max_length=100, default="user")
    password = models.CharField(max_length= 100)

    def __str__(self):
        return self.username
class Record(models.Model):
    path = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now=True)
    organization = models.CharField(max_length = 200)
    project_type = models.CharField(max_length = 200)