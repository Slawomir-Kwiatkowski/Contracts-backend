from rest_framework import routers
from .views import ContractUserViewSet, WarehouseViewSet

router = routers.DefaultRouter()
router.register("users", ContractUserViewSet, basename="user")
router.register("warehouses", WarehouseViewSet, basename="warehouse")
urlpatterns = router.urls
