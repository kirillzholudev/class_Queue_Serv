from django.contrib import admin

from main.models import Company, Order, Product, Worker, Client

admin.site.register(Company)
admin.site.register(Worker)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Client)
