from rest_framework import viewsets, response, status
from contracts.models import Contract
from ..serializers import ContractSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"client": self.request.user})
        return context
