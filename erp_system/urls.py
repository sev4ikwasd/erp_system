"""erp_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from proto import category_pb2_grpc, measure_unit_pb2_grpc, product_pb2_grpc
from data_handler.services import CategoryService, MeasureUnitService, ProductService

urlpatterns = [
    path('admin/', admin.site.urls),
]


def grpc_handlers(server):
    category_pb2_grpc.add_CategoryControllerServicer_to_server(CategoryService.as_servicer(), server)
    measure_unit_pb2_grpc.add_MeasureUnitControllerServicer_to_server(MeasureUnitService.as_servicer(), server)
    product_pb2_grpc.add_ProductControllerServicer_to_server(ProductService.as_servicer(), server)
