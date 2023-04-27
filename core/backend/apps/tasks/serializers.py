from rest_framework import serializers
from .models import Project, CheckPoint, Task
from ..data.serializers import TaskStatusSerializer
from ..crm.serializers import OrderSerializer
from ..res.serializers import ClientSerializer, EmployeeSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = []


class CheckPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckPoint
        exclude = ['id', ]


class TaskSerializer(serializers.ModelSerializer):
    status = TaskStatusSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    checkpoint = CheckPointSerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    order = OrderSerializer(read_only=True)
    init_empl = EmployeeSerializer(read_only=True)
    maker = EmployeeSerializer(read_only=True)

    class Meta:
        model = Task
        exclude = []
