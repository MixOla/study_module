from rest_framework.pagination import LimitOffsetPagination

from modules.models import Module
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)

from modules.serializers import ModuleSerializer


class ModuleCreateView(CreateAPIView):
    model = Module
    serializer_class = ModuleSerializer


class ModuleListView(ListAPIView):
    model = Module
    serializer_class = ModuleSerializer
    pagination_class = LimitOffsetPagination


class ModuleView(RetrieveUpdateDestroyAPIView):
    model = Module
    serializer_class = ModuleSerializer
    http_method_names = ['put', 'post', 'get', 'delete']

