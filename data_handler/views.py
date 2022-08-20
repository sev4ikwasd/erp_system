from django.views.decorators.csrf import csrf_exempt
from grpc_django.views import RetrieveGRPCView, ServerStreamGRPCView
from data_handler.models import Category, MeasureUnit, Product
from data_handler.serializers import CategorySerializer, MeasureUnitSerializer, ProductSerializer
from grpc_codegen.data_handler_pb2 import Category as CategoryProto, MeasureUnit as MeasureUnitProto, Product as ProductProto
from django.http import HttpResponse
from data_handler.producer import produce_parse_task


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


@csrf_exempt
def take_data_from_erp(request, slug):
    data = request.body.decode()
    produce_parse_task(slug, data)
    return HttpResponse(content="", status=200)
