from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    first_name =models.CharField(max_length=15,null=True,blank=True)
    last_name =models.CharField(max_length=15,null=True,blank=True)
    mobile_number = models.CharField(max_length=10,null=True,blank=True)
    gender_types=(
        (1,'Male'),
        (2,'Female'),
        (3,'Other'),
    )
    gender = models.IntegerField(
        choices=gender_types,
    )

class Orders(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    discount = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    placeat = models.CharField(max_length=200,null=True,blank=True)
    

