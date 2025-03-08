from rest_framework import viewsets
from .serializer import DashboardDataSerializer
from .models import DashboardData

class DashboardDataViewSet(viewsets.ModelViewSet):
    queryset = DashboardData.objects.all()
    serializer_class = DashboardDataSerializer