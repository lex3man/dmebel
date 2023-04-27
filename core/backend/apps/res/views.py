from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class GetRes(APIView):

    def get(self, _) -> Response:
        data = {"status": "OK"}
        return Response(data)

    def post(self, _) -> Response:
        data = {"status": "OK"}
        return Response(data)

