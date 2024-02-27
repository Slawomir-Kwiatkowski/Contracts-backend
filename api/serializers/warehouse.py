from rest_framework import serializers
from contracts.models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = ["warehouse_name", "warehouse_info"]

    def create(self, validated_data):
        validated_data["client"] = self.context["client"]
        contract = Warehouse.objects.create(**validated_data)
        return contract
