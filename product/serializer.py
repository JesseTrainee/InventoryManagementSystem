from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BulkProductSerializer(serializers.ModelSerializer):
    child = ProductSerializer

class ProductBulkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        list_serializer_class = BulkProductSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'

class BulkCategorySerializer(serializers.ListSerializer):
    child = CategorySerializer()

class CategoryBulkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        list_serializer_class = BulkCategorySerializer
