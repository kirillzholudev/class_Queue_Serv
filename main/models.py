from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import related


class Company(models.Model):
    name = models.CharField(max_length=80, verbose_name='Company name')
    adress = models.CharField(max_length=100, verbose_name='Company adress')

    def __str__(self):
        return f'{self.name}'


class Worker(models.Model):
    name = models.CharField(max_length=80, verbose_name='Employee Name')
    company = models.ForeignKey(Company, related_name='Company', on_delete=models.CASCADE)



class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, verbose_name='product_name')
    note = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ManyToManyField(Company)
    product_name = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.user} -- {self.company} -- {self.product_name}'


class Client(models.Model):
    name = models.CharField(max_length=80)
    service = models.ForeignKey(Product, related_name='services', on_delete=models.CASCADE)



