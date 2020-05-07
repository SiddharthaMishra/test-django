from rest_framework import viewsets

from .models import Model, Varient, Manufacturer
from .serializers import ManufacturerSerializer, CarModelSerializer, VarientSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = CarModelSerializer


class VarientViewSet(viewsets.ModelViewSet):
    queryset = Varient.objects.all()
    serializer_class = VarientSerializer