from django.db import models
from core.base_models import BaseModel
from product.models import Product
from users.models import User

class StockMovement(BaseModel):
    MOVEMENT_TYPE = [
        ('in', 'Entrada'),
        ('out', 'Saída'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movements")
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_movement_type_display()} por {self.user.username} em {self.timestamp}"

class StockTransaction(BaseModel):
    stock_movement = models.ForeignKey(StockMovement, on_delete=models.CASCADE, related_name="transactions")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_transaction = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} ({self.get_movement_type_display()})"
