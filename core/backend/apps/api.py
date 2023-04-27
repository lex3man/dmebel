from rest_framework.generics import ListAPIView
from .tasks.serializers import TaskSerializer
from .tasks import models


class GetData(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return models.Task.objects.all()
