from rest_framework.serializers import (
    Serializer,
    CharField,
)

class CommentSerializer(Serializer):
    tweet = CharField(max_length=100)