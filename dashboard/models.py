from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    np = models.CharField("Número de parte (NP)", max_length=100)
    serie = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    otros = models.TextField(blank=True, null=True)


    class Meta:
        verbose_name_plural ='Product'


    def __str__(self):
        return f"{self.name} - {self.marca}"
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='Order'

    def __str__(self):
        return f'Order #{self.id}'
