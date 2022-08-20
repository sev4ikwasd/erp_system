from django_grpc_framework import generics
from data_handler.models import Category, MeasureUnit, Product
from data_handler.serializers import CategoryProtoSerializer, MeasureUnitProtoSerializer, ProductProtoSerializer


class CategoryService(generics.ModelService):
    queryset = Category.objects.all()
    serializer_class = CategoryProtoSerializer


class MeasureUnitService(generics.ModelService):
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitProtoSerializer


class ProductService(generics.ModelService):
    queryset = Product.objects.all()
    serializer_class = ProductProtoSerializer
