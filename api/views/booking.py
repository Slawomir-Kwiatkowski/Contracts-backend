from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from contracts.models import Booking, Contract
from ..serializers import BookingSerializer
from ..permissions.booking import BookingWritePermission


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        BookingWritePermission
    ]

    def get_queryset(self):
        if self.request.user.profile == "client":
            contracts = Contract.objects.filter(client=self.request.user)
            return Booking.objects.filter(contract__in=contracts)
        elif self.request.user.profile == "contractor":
            contracts = Contract.objects.filter(contractor=self.request.user)
            return Booking.objects.filter(contract__in=contracts)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        contract = Contract.objects.get(id=serializer.data['contract'])
        contract.status = "accepted"
        contract.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
