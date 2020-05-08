from .models import Manufacturer, Variant, Model
from rest_framework import serializers



class ManufacturerSerializer(serializers.ModelSerializer):
    models = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Manufacturer
        fields = ['name', 'url', 'logo', 'models']
        read_only_fields = ['models']

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['name', 'manufacturer', "picture"]

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['name', 'model', 'price']

    