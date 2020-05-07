from .models import Manufacturer, Varient, Model
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
        fields = ['name', 'manufacturer']

class VarientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Varient
        fields = ['name', 'picture', 'model', 'width', 'height']

    