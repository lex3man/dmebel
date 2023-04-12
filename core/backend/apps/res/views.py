from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class GetRes(APIView):

    def get(self, _) -> Response:
        data = {"status": "OK"}
        return Response(data)

    def post(self, request) -> Response:
        data = {"status": "OK"}
        return Response(data)

