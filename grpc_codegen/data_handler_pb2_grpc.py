# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import data_handler_pb2 as data__handler__pb2


class ControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListCategories = channel.unary_stream(
                '/data_handler.Controller/ListCategories',
                request_serializer=data__handler__pb2.CategoryListRequest.SerializeToString,
                response_deserializer=data__handler__pb2.Category.FromString,
                )
        self.RetrieveCategory = channel.unary_unary(
                '/data_handler.Controller/RetrieveCategory',
                request_serializer=data__handler__pb2.CategoryRetrieveRequest.SerializeToString,
                response_deserializer=data__handler__pb2.Category.FromString,
                )
        self.ListMeasureUnits = channel.unary_stream(
                '/data_handler.Controller/ListMeasureUnits',
                request_serializer=data__handler__pb2.MeasureUnitListRequest.SerializeToString,
                response_deserializer=data__handler__pb2.MeasureUnit.FromString,
                )
        self.RetrieveMeasureUnit = channel.unary_unary(
                '/data_handler.Controller/RetrieveMeasureUnit',
                request_serializer=data__handler__pb2.MeasureUnitRetrieveRequest.SerializeToString,
                response_deserializer=data__handler__pb2.MeasureUnit.FromString,
                )
        self.ListProducts = channel.unary_stream(
                '/data_handler.Controller/ListProducts',
                request_serializer=data__handler__pb2.ProductListRequest.SerializeToString,
                response_deserializer=data__handler__pb2.Product.FromString,
                )
        self.RetrieveProduct = channel.unary_unary(
                '/data_handler.Controller/RetrieveProduct',
                request_serializer=data__handler__pb2.ProductRetrieveRequest.SerializeToString,
                response_deserializer=data__handler__pb2.Product.FromString,
                )


class ControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListCategories(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMeasureUnits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveMeasureUnit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListCategories': grpc.unary_stream_rpc_method_handler(
                    servicer.ListCategories,
                    request_deserializer=data__handler__pb2.CategoryListRequest.FromString,
                    response_serializer=data__handler__pb2.Category.SerializeToString,
            ),
            'RetrieveCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveCategory,
                    request_deserializer=data__handler__pb2.CategoryRetrieveRequest.FromString,
                    response_serializer=data__handler__pb2.Category.SerializeToString,
            ),
            'ListMeasureUnits': grpc.unary_stream_rpc_method_handler(
                    servicer.ListMeasureUnits,
                    request_deserializer=data__handler__pb2.MeasureUnitListRequest.FromString,
                    response_serializer=data__handler__pb2.MeasureUnit.SerializeToString,
            ),
            'RetrieveMeasureUnit': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveMeasureUnit,
                    request_deserializer=data__handler__pb2.MeasureUnitRetrieveRequest.FromString,
                    response_serializer=data__handler__pb2.MeasureUnit.SerializeToString,
            ),
            'ListProducts': grpc.unary_stream_rpc_method_handler(
                    servicer.ListProducts,
                    request_deserializer=data__handler__pb2.ProductListRequest.FromString,
                    response_serializer=data__handler__pb2.Product.SerializeToString,
            ),
            'RetrieveProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveProduct,
                    request_deserializer=data__handler__pb2.ProductRetrieveRequest.FromString,
                    response_serializer=data__handler__pb2.Product.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'data_handler.Controller', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Controller(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListCategories(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/data_handler.Controller/ListCategories',
            data__handler__pb2.CategoryListRequest.SerializeToString,
            data__handler__pb2.Category.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_handler.Controller/RetrieveCategory',
            data__handler__pb2.CategoryRetrieveRequest.SerializeToString,
            data__handler__pb2.Category.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMeasureUnits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/data_handler.Controller/ListMeasureUnits',
            data__handler__pb2.MeasureUnitListRequest.SerializeToString,
            data__handler__pb2.MeasureUnit.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveMeasureUnit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_handler.Controller/RetrieveMeasureUnit',
            data__handler__pb2.MeasureUnitRetrieveRequest.SerializeToString,
            data__handler__pb2.MeasureUnit.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/data_handler.Controller/ListProducts',
            data__handler__pb2.ProductListRequest.SerializeToString,
            data__handler__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_handler.Controller/RetrieveProduct',
            data__handler__pb2.ProductRetrieveRequest.SerializeToString,
            data__handler__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
