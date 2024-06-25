from django.db import models

# Create your models here.
class VehicleModel(models.Model):
    FullName=models.CharField(
        max_length=255
    )
    VehicleNumber=models.CharField(
        max_length=15
    )
    
    def __str__(self):
        return"{}. {}".format(self.id, self.VehicleNumber)