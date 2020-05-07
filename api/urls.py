from rest_framework import routers

from .views import VarientViewSet, ManufacturerViewSet, ModelViewSet

router = routers.DefaultRouter()

router.register('models', ModelViewSet)
router.register('varients', VarientViewSet)
router.register('manufacturers', ManufacturerViewSet)

urlpatterns = router.urls