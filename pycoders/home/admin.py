from django.contrib import admin
from .models import Customer, Brand, Product, Category, Store, TimeStamp, DataAnalyst

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','brand','description','price')
    search_fields = ('id', 'name','brand','category')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','contact_no','address','city','dob')
    search_fields = ('id', 'first_name','last_name','city')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('id','name','location','email','contact_no')
    search_fields = ('id', 'name','location')




admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Store, StoreAdmin)
admin.site.register(TimeStamp)
admin.site.register(DataAnalyst)

