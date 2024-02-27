from rest_framework import serializers
from contracts.models import Booking


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "contract",
            "pallets_actual",
            "driver_full_name",
            "driver_phone_number",
            "truck_reg_number",
        ]
