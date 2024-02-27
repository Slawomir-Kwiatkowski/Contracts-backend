from rest_framework import serializers
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    # warehouse = serializers.StringRelatedField()
    date_of_order = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    time_of_delivery = serializers.TimeField(format="%H:%M")

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["contractor"] = instance.contractor
        return repr

    def create(self, validated_data):
        validated_data["client"] = self.context["client"]
        contract = Contract.objects.create(**validated_data)
        return contract

    class Meta:
        model = Contract
        fields = [
            "status",
            "contract_number",
            "client",
            "contractor",
            "date_of_order",
            "date_of_delivery",
            "time_of_delivery",
            "pallets_planned",
            "warehouse",
        ]
