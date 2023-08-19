from rest_framework.serializers import (
    Serializer,
    CharField,
)

class ClientSerializer(Serializer):
    name = CharField(max_length=100)
    domain = CharField(max_length=100)