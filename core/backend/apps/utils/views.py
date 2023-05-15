from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from .models import Bot
from .serializers import BotSerializer


class Bots(APIView):

    def get(self, _) -> Response:
        data = {"status": "OK"}
        return Response(data)

    def post(self, _) -> Response:
        data = {"status": "OK"}
        return Response(data)


class BotConf(RetrieveUpdateAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

