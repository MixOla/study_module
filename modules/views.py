from rest_framework.pagination import LimitOffsetPagination

from modules.models import Module
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)

from modules.serializers import ModuleSerializer


class ModuleCreateView(ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleView(RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


