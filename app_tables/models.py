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
    Email=models.EmailField(
        unique=True
    )
    Address=models.TextField()
    Created_at=models.DateField(
        auto_now_add=True
    )
    Updated_at=models.DateField(
        auto_now=True
    )
    
    def __str__(self):
        return"{}. {}".format(self.id, self.FullName)
    
class OutletModel(models.Model):
    OutletNumber=models.CharField(
        max_length=255
    )
    OutletCode=models.CharField(
        max_length=255
    )
    OutletName=models.CharField(
        max_length=255
    )
    OutletType=models.CharField(
        max_length=255
    )
    Address1=models.CharField(
        max_length=255
    )
    Address2=models.CharField(
        max_length=255
    )
    Town=models.CharField(
        max_length=255
    )
    Provinsi=models.CharField(
        max_length=255
    )
    Kabupaten=models.CharField(
        max_length=255
    )
    Kecamatan=models.CharField(
        max_length=255
    )
    Kelurahan=models.CharField(
        max_length=255
    )
    Latitude=models.CharField(
        max_length=255
    )
    Longitude=models.CharField(
        max_length=255
    )
    Days=models.CharField(
        max_length=255
    )
    Delivery=models.CharField(
        max_length=255
    )