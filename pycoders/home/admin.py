from django.contrib import admin
from .models import Customer, Brand, Product, Category, Store

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Store)


