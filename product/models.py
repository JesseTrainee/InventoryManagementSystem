from django.db import models
from core.base_models import BaseModel

class Category(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Product(BaseModel):
    name = models.CharField(max_length=300, blank=False, null=False)
    code = models.CharField(max_length=100, unique=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.code})"
