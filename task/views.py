from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import Task_Serializer
from .models import *


# Create your views here.
class task_api_view(APIView):
    def get(self, request, id=None):
        if id is not None:
            task = get_object_or_404(Task, id=id)
            task_serialize = Task_Serializer(task)
            return Response(task_serialize.data)
        else:
            task = Task.objects.all()
            task_serialize = Task_Serializer(task, many=True)
            return Response(task_serialize.data)
    
    def post(self, request, id=None):
        data = request.data
        data_serialize = Task_Serializer(data=data)
        if data_serialize.is_valid():
            data_serialize.save()
            message = "New Task Added Successfully!"
            return Response(message)
        else:
            return Response(data_serialize.errors)
    
    def put(self, request, id):
        data = request.data
        task = get_object_or_404(Task, id=id)
        task_serialize = Task_Serializer(task, data=data)
        if task_serialize.is_valid():
            task_serialize.save()
            message = "Task Full Updated Successfully!"
            return Response(message)
        else:
            return Response(task_serialize.errors)
    
    def patch(self, request, id):
        data = request.data
        task = get_object_or_404(Task, id=id)
        task_serialize = Task_Serializer(task, data=data, partial=True)
        if task_serialize.is_valid():
            task_serialize.save()
            message = "Task Partial Updated Successfully!"
            return Response(message)
        else:
            return Response(task_serialize.errors)
    
    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        message = "Task Delete Successfully!"
        return Response(message)

