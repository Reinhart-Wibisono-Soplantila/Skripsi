from django.db import models
from django.utils import timezone

# Create your models here.
class VehicleModel(models.Model):
    UnitType=models.CharField(
        max_length=255
    )
    VehicleNumber=models.CharField(
        max_length=20,
        unique=True,
    )
    Status=models.CharField(
        max_length=20,
        default='Ready'
    )
    Created_at=models.DateField(
        auto_now_add=True
    )
    Updated_at=models.DateField(
        auto_now=True
    )
    
    def __str__(self):
        return"{}. {}".format(self.id, self.VehicleNumber)
    
class DriverModel(models.Model):
    FullName=models.CharField(
        max_length=255
    )
    Phone=models.CharField(
        max_length=30
    )
    Email=models.EmailField()
    Address=models.TextField()
    Created_at=models.DateField(
        auto_now_add=True
    )
    Updated_at=models.DateField(
        auto_now=True
    )
    