from rest_framework.serializers import ModelSerializer

from data_handler.models import Category, MeasureUnit, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category


class MeasureUnitSerializer(ModelSerializer):
    class Meta:
        model = MeasureUnit


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
