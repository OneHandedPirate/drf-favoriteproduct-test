from rest_framework import serializers


class DefaultResponseSerializer(serializers.Serializer):
    detail = serializers.CharField(read_only=True)


class EmptyResponseSerializer(serializers.Serializer): ...
