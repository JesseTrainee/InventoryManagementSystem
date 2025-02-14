from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product.views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename="Produtos")
router.register('category', CategoryViewSet, basename="Categoria")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
