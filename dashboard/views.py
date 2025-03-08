from rest_framework import viewsets
from .models import DashboardData
from .serializer import DashboardDataSerializer
class DashboardDataViewSet(viewsets.ModelViewSet):
    queryset = DashboardData.objects.all()
    serializer_class = DashboardDataSerializer