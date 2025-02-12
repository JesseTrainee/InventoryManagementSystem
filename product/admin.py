from django.contrib import admin
from product.models import Product

class Products(admin.ModelAdmin):
    list_diplay = ('name', 'category', 'quantity', 'price')
    list_display_link = ('name',)
    list_per_page = 20
    search_fields = ('name',)

admin.site.register(Product, Products)