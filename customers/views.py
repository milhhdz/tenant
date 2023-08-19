from customers.models import Client, Domain
from customers.serializers import ClientSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_500_INTERNAL_SERVER_ERROR
)

# Create your views here.
class CreateTenantView(APIView):

    name:str = None
    domain:str = None
    schema_name:str = None

    client:Client = None

    response:Response = None

    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.name = serializer.validated_data.get('name')
        self.domain = serializer.validated_data.get('domain')

        self.create_schema()

        if not self.is_created_client():
            return self.response
        
        if not self.is_created_domain():
            return self.response
        
        return self.response

    
    def create_schema(self):
        self.schema_name = '_'.join(self.domain.split('.'))
    
    def is_created_client(self) -> bool:
        try:
            self.client_ = Client.objects.create(
                name=self.name,
                schema_name=self.schema_name
            )
        except Exception as e:
            print(e)
            self.response = Response({
                'message': 'Error creating client'
            }, status=HTTP_500_INTERNAL_SERVER_ERROR)
            return False
        return True
    
    def is_created_domain(self) -> bool:
        try:
            Domain.objects.create(
                domain=self.domain,
                tenant=self.client_,
                is_primary=True
            )

            self.response = Response({
                'message': 'Client created successfully'
            }, status=HTTP_201_CREATED)
        except Exception as e:
            print(e)
            self.response = Response({
                'message': 'Error creating domain'
            }, status=HTTP_500_INTERNAL_SERVER_ERROR)
            return False
        return True
    