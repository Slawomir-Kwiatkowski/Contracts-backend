from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from contracts.models import Contract
from ..serializers import ContractSerializer
from ..permissions.contract import ContractWritePermission


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        ContractWritePermission
    ]

    def get_queryset(self):
        if self.request.user.profile == "client":
            return Contract.objects.filter(client=self.request.user)
        elif self.request.user.profile == "contractor":
            return Contract.objects.filter(contractor=self.request.user)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"client": self.request.user})
        return context
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == "open":
            # instance.delete()         // if instance should be deleted - default option
            # return Response(status=status.HTTP_204_NO_CONTENT)
            instance.status = "cancelled"
            instance.save()
            return Response({"msg": "Contract succesfully cancelled"}, status=status.HTTP_200_OK)
        else: 
            error_msg = f"Bad request. Contract status: '{instance.status}'"
            return Response({"error": error_msg}, status=status.HTTP_400_BAD_REQUEST)
