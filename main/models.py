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
    overtimeNumber = models.IntegerField(null=True)
    

    def __str__(self):
        return self.firstName + " " + self.lastName
    
class Day(models.Model):
    dayName = models.CharField(max_length=30, null=True)
    date = models.DateField(null=True)
    numDeliveries = models.IntegerField(null=True)
    helper = models.CharField(max_length=500, null=True)
    driver = models.CharField(max_length=500, null=True)
    pay = None
    storeNum = models.IntegerField(null=True)
    storeNum2 = models.IntegerField(null=True, default=None)
    saturday = models.DateField(null=True)
    truck = models.CharField(max_length=500, null=False)
    isOff = models.NullBooleanField(null= True, default = False)
    
    def __str__(self):
        date = str(self.date)
        truckName = str(self.truck)
        result = date + "--" + truckName
        return result

class Store(models.Model):
    storeNumber = models.IntegerField()
    
    def __str__(self):
        return str(self.storeNumber)