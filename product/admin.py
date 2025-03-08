from django.contrib import admin
from product.models import Product, Category

class Products(admin.ModelAdmin):
    list_diplay = ('name', 'category', 'quantity', 'price')
    list_display_link = ('name',)
    list_per_page = 20
    search_fields = ('name',)

admin.site.register(Product, Products)

class Categories(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_link = ('title',)
    list_per_page = 20
    search_fields = ('title',)

admin.site.register(Category, Categories)