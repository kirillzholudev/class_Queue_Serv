from django.db import models
from main.models import Worker, Product, Company, Client


class Register_on_shift(models.Model):
    service = models.ForeignKey(Product, related_name='process', on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, related_name='worker', on_delete=models.CASCADE)
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(auto_now_add=False)


class Process_worker(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client.name}:{self.time}'


class Register_in_queue(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client.name}--{self.service.name}--{self.time}'

