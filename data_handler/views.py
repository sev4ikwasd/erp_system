from grpc_django.views import RetrieveGRPCView, ServerStreamGRPCView
from data_handler.models import Category, MeasureUnit, Product
from data_handler.serializers import CategorySerializer, MeasureUnitSerializer, ProductSerializer
from grpc_codegen.data_handler_pb2 import Category as CategoryProto, MeasureUnit as MeasureUnitProto, Product as ProductProto


class RetrieveCategory(RetrieveGRPCView):
    queryset = Category.objects.all()
    response_proto = CategoryProto
    serializer_class = CategorySerializer


class ListCategories(ServerStreamGRPCView):
    queryset = Category.objects.all()
    response_proto = CategoryProto
    serializer_class = CategorySerializer


class RetrieveMeasureUnit(RetrieveGRPCView):
    queryset = MeasureUnit.objects.all()
    response_proto = MeasureUnitProto
    serializer_class = MeasureUnitSerializer


class ListMeasureUnits(ServerStreamGRPCView):
    queryset = MeasureUnit.objects.all()
    response_proto = MeasureUnitProto
    serializer_class = MeasureUnitSerializer


class RetrieveProduct(RetrieveGRPCView):
    queryset = Product.objects.all()
    response_proto = ProductProto
    serializer_class = ProductSerializer


class ListProducts(ServerStreamGRPCView):
    queryset = Product.objects.all()
    response_proto = ProductProto
    serializer_class = ProductSerializer
