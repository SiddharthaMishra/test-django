from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import views, settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('', views.ManufacturerList.as_view(), name='index'),
    path('<int:pk>', views.ManufacturerDetail.as_view(), name='manufacturer-detail'),
    path('models/<int:pk>', views.ModelDetail.as_view(), name="model-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
