from django.contrib import admin

from main.models import Company, Order, Product

admin.site.register(Company)
admin.site.register(Order)
admin.site.register(Product)