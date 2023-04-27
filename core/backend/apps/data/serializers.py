from rest_framework import serializers
from .models import ClientStatus, Tag, ContactMethod, AdminRole, EmployeeRole, TaskStatus


class ClientStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientStatus
        exclude = ['id', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['id', ]


class ContactMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMethod
        exclude = ['id', ]


class AdminRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminRole
        exclude = ['id', ]


class EmployeeRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRole
        exclude = ['id', ]


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        exclude = ['id', ]
