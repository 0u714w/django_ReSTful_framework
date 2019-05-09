from rest_framework import serializers
from project.models import Manufacturer, ShoeType, ShoeColor, Shoe

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'url',)

class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('style',)

class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('color_name',)

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = ('id', 'size', 'brand_name', 'manufacturer', 'color', 'material', 'shoe_type', 'fasten_type',)