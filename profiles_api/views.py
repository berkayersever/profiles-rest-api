from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        api_view = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URL\'s',
        ]

        return Response({'message': 'Hello!', 'api_view': api_view})
