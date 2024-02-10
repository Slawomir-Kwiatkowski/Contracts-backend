from rest_framework import viewsets
from users.models import ContractUser
from ..serializers import ContractUserSerializer


class ContractUserViewSet(viewsets.ModelViewSet):
    queryset = ContractUser.objects.all()
    serializer_class = ContractUserSerializer
