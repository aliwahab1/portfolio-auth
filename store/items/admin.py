from itertools import product
from django.contrib import admin

# Register your models here.
from .models import *

class ProductAdmin(models.Model):
    list_display=('name', 'price', 'slug', 'date')
    list_filter=('name', 'date', 'price')
    prepopulated_field = {'slug' : ('name',)}

admin.site.register(Product, ProductAdmin)