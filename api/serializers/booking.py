from rest_framework import serializers
from contracts.models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = [
            "id",
            "contract",
            "pallets_actual",
            "driver_full_name",
            "driver_phone_number",
            "truck_reg_number",
        ]

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)
