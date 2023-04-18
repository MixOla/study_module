from rest_framework import serializers

from modules.models import Module


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = '__all__'
        read_only_fields = '__all__'