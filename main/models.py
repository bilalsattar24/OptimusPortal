from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Truck(models.Model):
    truckName = models.CharField(max_length=250)
    
    def __str__(self):
        return "Truck Name: " + self.truckName + " - ID = " + str(self.id)
    
    
class Employee(models.Model):
    firstName = models.CharField(max_length=500)
    lastName = models.CharField(max_length=500)
    role = models.CharField(max_length=500)

    
class Day(models.Model):
    dayName = models.CharField(max_length=30)
    date = models.DateField()
    numDeliveries = models.IntegerField()
    helper = models.CharField(max_length=500)
    driver = models.CharField(max_length=500)
    pay = None
    storeNum = models.IntegerField()
    saturday = models.DateField()
    