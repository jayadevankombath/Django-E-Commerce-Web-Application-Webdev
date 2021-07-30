from django.db import models
from django.db.models.fields import CharField

class Userlogin(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.IntegerField(default=100)
class Adminlogin(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.IntegerField(default=100)
class Product(models.Model):
    Product_name = models.CharField(max_length=50)
    Product_color = models.CharField(max_length=100)
    Product_brand = models.CharField(max_length=100)
    Product_size = models.IntegerField(default=100)
    Product_price = models.DecimalField(max_digits=10,decimal_places=2)
    Product_photo = models.CharField(max_length=50)
class Stock(models.Model):
    Product_id = models.IntegerField(default=100)
    P_quantity = models.IntegerField(default=100)
class Purchase(models.Model):
    Product_id = models.IntegerField(default=100)
    Pur_date = models.DateField()
    Pur_quantity = models.IntegerField(default=100)
    Pur_price = models.DecimalField(max_digits=10,decimal_places=2)
    Pur_amount = models.DecimalField(max_digits=10,decimal_places=2)
class Sales(models.Model):
    Product_id = models.IntegerField(default=100)
    Sale_quantity = models.IntegerField(default=100)
    Sale_amount = models.DecimalField(max_digits=10,decimal_places=2)
