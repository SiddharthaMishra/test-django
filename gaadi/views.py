from api.models import Manufacturer, Variant, Model
from api.serializers import ManufacturerSerializer, VariantSerializer, CarModelSerializer

from django.shortcuts import redirect, get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class ManufacturerList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = Manufacturer.objects.all()
        return Response({'manufacturers': queryset, 'serializer': ManufacturerSerializer})

    def post(self, request):
        serializer = ManufacturerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'manufacturer': Manufacturer.objects.all()})
        serializer.save()
        return redirect('index')



class ManufacturerDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'models.html'

    def get(self, request, pk):
        manufacturer = get_object_or_404(Manufacturer, pk=pk)
        serializer = CarModelSerializer()
        return Response({'serializer': serializer, 'manufacturer': manufacturer})

    def post(self, request, pk):
        manufacturer = get_object_or_404(Manufacturer, pk=pk)
        serializer = CarModelSerializer(data=request.data)
        if not serializer.is_valid():
            return redirect('manufacturer-detail', pk=pk)
        serializer.save()
        return redirect('manufacturer-detail', pk=pk)
    
    def delete(self, request, pk):
        manufacturer = get_object_or_404(Manufacturer, pk=pk)
        manufacturer.delete()
        return redirect('index')


class ModelDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'variants.html'

    def get(self, request, pk):
        model = get_object_or_404(Model, pk=pk)
        serializer = VariantSerializer()
        return Response({'serializer': serializer, 'model': model})

    def post(self, request, pk):
        model = get_object_or_404(Model, pk=pk)
        serializer = VariantSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'model': model})
        serializer.save()
        return redirect('model-detail', pk=pk)
    
    def delete(self, request, pk):
        model = get_object_or_404(Model, pk=pk)
        parent = model.manufacturer
        model.delete()
        return redirect('manufacturer-detail', pk=model.pk)
