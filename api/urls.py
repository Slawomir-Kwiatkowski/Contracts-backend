from rest_framework import routers
from .views import (
    ContractUserViewSet,
    WarehouseViewSet,
    ContractViewSet,
    BookingViewSet,
)

router = routers.DefaultRouter()
router.register("users", ContractUserViewSet, basename="user")
router.register("warehouses", WarehouseViewSet, basename="warehouse")
router.register("contracts", ContractViewSet, basename="contract")
router.register("bookings", BookingViewSet, basename="booking")
urlpatterns = router.urls
