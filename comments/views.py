from comments.models import Comment
from comments.serializers import CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_500_INTERNAL_SERVER_ERROR
)

# Create your views here.
class CreateComment(APIView):
    tweet:str = None
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            Comment.objects.create(
                tweet=serializer.validated_data.get('tweet')
            )
        except Exception as e:
            print(e)
            return Response({
                'message': 'Error creating comment'
            }, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({
            'message': 'Comment created successfully'
        }, status=HTTP_201_CREATED)