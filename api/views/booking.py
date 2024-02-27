from rest_framework import viewsets
from contracts.models import Booking, Contract
from ..serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        contract_number = self.request.POST.get("contract")
        contract = Contract.objects.filter(contract_number=contract_number).first()
        context.update({"contract": contract})
        return context
