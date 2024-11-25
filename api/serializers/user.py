from rest_framework import serializers, validators
from users.models import ContractUser


class ContractUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractUser
        fields = "__all__"
        # fields = ("username", "password", "email", "profile")
        extra_kwargs = {
            "username": {"min_length": 6, "max_length": 25},
            "password": {"write_only": True, "min_length": 6, "max_length": 25},
        }

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
