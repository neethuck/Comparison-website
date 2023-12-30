from django.db import models
from django.contrib.auth.models import User


from django.db import models

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    brand_img = models.ImageField(upload_to='brand',null=True,blank=True)
    Description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.brand_name
    
    

class Mobile(models.Model):
    phone_id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, db_column='brand_id')
    model_name = models.CharField(max_length=100)
    Img = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    display_size = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=100,null=True, blank=True)
    RAM = models.CharField(max_length=100,null=True, blank=True)
    internal_storage = models.CharField(max_length=100,null=True, blank=True)
    is_free_delivary_available = models.BooleanField(default=True)
    is_in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand.brand_name} {self.model_name}"


