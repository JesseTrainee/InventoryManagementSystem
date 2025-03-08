from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product.views import ProductViewSet, CategoryViewSet
from stock.views import StockMovementViewSet, StockTransactionViewSet
from dashboard.views import DashboardDataViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename="Produtos")
router.register('category', CategoryViewSet, basename="Categoria")
router.register('stock-transaction', StockTransactionViewSet, basename="Transação de Estoque")
router.register('stock-movement', StockMovementViewSet, basename="Movimentação de Estoque")
router.register('dashboard', DashboardDataViewSet, basename="Dashboard ")
router.register('user', UserViewSet, basename="Usuário ")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
