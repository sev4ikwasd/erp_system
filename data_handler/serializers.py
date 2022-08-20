from django_grpc_framework import proto_serializers
from data_handler.models import Category, MeasureUnit, Product
from proto import category_pb2, measure_unit_pb2, product_pb2


class CategoryProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Category
        proto_class = category_pb2.Category


class MeasureUnitProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = MeasureUnit
        proto_class = measure_unit_pb2.MeasureUnit


class ProductProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class = product_pb2.Product
