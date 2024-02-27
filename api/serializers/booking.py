from rest_framework import serializers
from contracts.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField(many=False)

    def validate(self, data):
        data["contract"] = self.context["contract"]
        super().validate(data)
        return data

    def create(self, validated_data):
        if not Booking.objects.filter(contract=validated_data["contract"]):
            booking = Booking.objects.create(**validated_data)
            return booking
        else:
            raise serializers.ValidationError(detail={"detail": "Booking not created"})

    class Meta:
        model = Booking
        fields = [
            "contract",
            "pallets_actual",
            "driver_full_name",
            "driver_phone_number",
            "truck_reg_number",
        ]
