from rest_framework import serializers
from users.models import ContractUser


class ContractUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractUser
        # fields = "__all__"
        fields = ("username", "password", "email", "profile")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = ContractUser(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        if "profile" in validated_data:
            user.profile = validated_data["profile"]
        user.set_password(validated_data["password"])
        user.save()
        return user
