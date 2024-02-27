from rest_framework import serializers
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "status",
            "contract_number",
            "client",
            "contractor",
            "date_od_order",
            "date_of_delivery",
            "time_of_delivery",
            "pallets_planned",
            "warehouse",
        ]
