from rest_framework import serializers
from .models import Task

class Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority']

