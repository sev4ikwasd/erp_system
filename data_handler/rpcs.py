from grpc_django.interfaces import rpc
from data_handler.views import RetrieveCategory, ListCategories, RetrieveMeasureUnit, ListMeasureUnits, RetrieveProduct, ListProducts

rpcs = [
    rpc(name='RetrieveCategory', view=RetrieveCategory),
    rpc(name='ListCategories', view=ListCategories),
    rpc(name='RetrieveMeasureUnit', view=RetrieveMeasureUnit),
    rpc(name='ListMeasureUnits', view=ListMeasureUnits),
    rpc(name='RetrieveProduct', view=RetrieveProduct),
    rpc(name='ListProducts', view=ListProducts),
]
