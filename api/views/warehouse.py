from rest_framework import viewsets
from contracts.models import Warehouse
from ..serializers import WarehouseSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"client": self.request.user})
        return context
