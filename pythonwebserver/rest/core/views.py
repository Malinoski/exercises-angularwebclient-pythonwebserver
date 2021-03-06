from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # to protect the api


class HelloView(APIView):

    permission_classes = (IsAuthenticated,)  # to protect the api

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
