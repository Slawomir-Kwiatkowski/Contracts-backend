from rest_framework import serializers
from contracts.models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = ["id", "warehouse_name", "warehouse_info"]

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["client"] = self.context["client"]
        return super().create(validated_data)
