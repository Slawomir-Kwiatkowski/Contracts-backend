from rest_framework import serializers
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            "id",
            "status",
            "contract_number",
            "client",
            "contractor",
            "date_of_order",
            "date_of_delivery",
            "time_of_delivery",
            "pallets_planned",
            "warehouse",
            "warehouse_info"
        ]
        extra_kwargs = {
            "status": {"read_only": True},
            "date_of_order": {
                "read_only": True,
                "format": "%Y-%m-%d"
            },
            "time_of_delivery": {"format": "%H:%M"},
        }

    client = serializers.StringRelatedField()
    warehouse_info = serializers.SerializerMethodField()

    def validate(self, attrs):
        return super().validate(attrs)

    def get_warehouse_info(self, obj):
        return obj.warehouse.warehouse_info

    def to_representation(self, instance):
        contract = super().to_representation(instance)
        contract['contractor'] = instance.contractor.username
        contract['warehouse'] = instance.warehouse.warehouse_name
        return contract


    def create(self, validated_data):
        validated_data["client"] = self.context["client"]
        contract = Contract.objects.create(**validated_data)
        return contract