from django.contrib.auth.models import User
from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='company_name')
    adres = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'



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

