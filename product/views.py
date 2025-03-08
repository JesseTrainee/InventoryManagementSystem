from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer, CategoryBulkCreateSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CategoryBulkCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryBulkCreateSerializer
