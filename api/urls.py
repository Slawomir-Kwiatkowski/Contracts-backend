from rest_framework import routers
from .views import WarehouseViewSet, ContractViewSet, BookingViewSet, UserViewSet


router = routers.DefaultRouter()
router.register("user", UserViewSet, basename="user")
router.register("warehouses", WarehouseViewSet, basename="warehouse")
router.register("contracts", ContractViewSet, basename="contract")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = router.urls
