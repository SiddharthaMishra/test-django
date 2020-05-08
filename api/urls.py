from rest_framework import routers

from .views import VariantViewSet, ManufacturerViewSet, ModelViewSet

router = routers.DefaultRouter()

router.register('models', ModelViewSet)
router.register('variants', VariantViewSet, basename="variant")
router.register('manufacturers', ManufacturerViewSet)

urlpatterns = router.urls