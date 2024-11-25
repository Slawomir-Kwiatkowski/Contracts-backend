from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from contracts.models import Warehouse
from ..serializers import WarehouseSerializer
from ..permissions.warehouse import WarehouseWritePermission


class WarehouseViewSet(viewsets.ModelViewSet):
    # queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated, WarehouseWritePermission]

    def get_queryset(self):
        user = self.request.user
        return Warehouse.objects.filter(client=user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"client": self.request.user})
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
