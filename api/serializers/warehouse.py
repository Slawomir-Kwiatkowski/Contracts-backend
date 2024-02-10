from rest_framework import serializers
from contracts.models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["warehouse_name", "warehouse_info", "client"]
