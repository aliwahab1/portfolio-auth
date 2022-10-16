from itertools import product
from django.contrib import admin
from models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','slug','date')
    list_filter=('name', 'date', 'price')
    prepopulated_fields={'slug' : ('name',)}


admin.site.register(product, ProductAdmin)