from rest_framework import serializers
from .models import Client, Employee, Admin, Human
from ..data.serializers import ClientStatusSerializer, TagSerializer, ContactMethodSerializer, AdminRoleSerializer, EmployeeRoleSerializer


class HumanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Human
        exclude = []


class ClientSerializer(serializers.ModelSerializer):
    human = HumanSerializer(read_only=True)
    status = ClientStatusSerializer(read_only=True)
    method = ContactMethodSerializer(read_only=True)
    tag = TagSerializer(read_only=True, many=True)
    
    class Meta:
        model = Client
        exclude = []


class EmployeeSerializer(serializers.ModelSerializer):
    human = HumanSerializer(read_only=True)
    role = EmployeeRoleSerializer(read_only=True)
    tag = TagSerializer(read_only=True, many=True)
    
    class Meta:
        model = Employee
        exclude = []


class AdminSerializer(serializers.ModelSerializer):
    human = HumanSerializer(read_only=True)
    role = AdminRoleSerializer(read_only=True)

    class Meta:
        model = Admin
        exclude = []
    
