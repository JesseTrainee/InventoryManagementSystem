from django.db import models
from core.base_models import BaseModel

class DashboardData(BaseModel):
    total_products = models.PositiveIntegerField(default=0)
    total_categories = models.PositiveIntegerField(default=0)
    total_stock_value = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dashboard atualizado em: {self.last_updated}"
