from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from .forms import Task_Form, Task_Photo_Form
from .models import Task, Task_Photo
from .serializer import Task_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
from django.db.models import Case, When, IntegerField
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os

class task_api_view(APIView):
    def get(self, request, id=None, format=None):
        if id is not None:
            task = get_object_or_404(Task, id=id)
            task_serialize = Task_Serializer(task)
            return Response(task_serialize.data)
        else:
            task = Task.objects.all()
            task_serialize = Task_Serializer(task, many=True)
            return Response(task_serialize.data)
    
    def post(self, request, format=None):
        data = request.data
        data_serialize = Task_Serializer(data=data)
        if data_serialize.is_valid():
            data_serialize.save()
            message = "New Task Added Successfully!"
            return Response(message)
        else:
            return Response(data_serialize.errors)
    
    def put(self, request, id, format=None):
        data = request.data
        task = get_object_or_404(Task, id=id)
        task_serialize = Task_Serializer(task, data=data)
        if task_serialize.is_valid():
            task_serialize.save()
            message = "Task Full Updated Successfully!"
            return Response(message)
        else:
            return Response(task_serialize.errors)
    
    def patch(self, request, id, format=None):
        data = request.data
        task = get_object_or_404(Task, id=id)
        task_serialize = Task_Serializer(task, data=data, partial=True)
        if task_serialize.is_valid():
            task_serialize.save()
            message = "Task Partial Updated Successfully!"
            return Response(message)
        else:
            return Response(task_serialize.errors)
    
    def delete(self, request, id, format=None):
        task = get_object_or_404(Task, id=id)
        task.delete()
        message = "Task Delete Successfully!"
        return Response(message)


class index(LoginRequiredMixin, generic.TemplateView):
    template_name = 'task/index.html'
    def get(self, request):
        context = {}
    
        filter = request.GET.get('filter')
        if filter:
            context['filter'] = filter
        search_value = request.GET.get('search_key')
        
        if search_value:
            task = Task.objects.filter(title__icontains=search_value)
        elif filter == 'id':
            task = Task.objects.all().order_by('id')
        elif filter == 'priority':
            task = Task.objects.all().order_by(
                Case(
                        When(priority='High', then=1),
                        When(priority='Medium', then=2),
                        When(priority='Low', then=3),
                        default=4,
                        output_field=IntegerField()
                    ),
            )
        elif filter == 'due_date':
            task = Task.objects.all().order_by('due_date')
        elif filter == 'created_date':
            task = Task.objects.all().order_by('-created_date')
        elif filter == 'complete':
            task = Task.objects.filter(is_complete=True)
        elif filter == 'incomplete':
            task = Task.objects.filter(is_complete=False)
        else:
            task = Task.objects.all()
        context['task'] = task
        return render(request, self.template_name, context)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = Task_Form
    context_object_name = 'tasks'
    template_name = 'task/add_task.html'
    success_url = reverse_lazy('index')


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = Task_Form
    context_object_name = 'tasks'
    template_name = 'task/add_task.html'
    def get_success_url(self) -> str:
        return reverse_lazy('task_details', kwargs={'id': self.object.pk})



class Delete_Image(LoginRequiredMixin, View):
    def get(self, request, id):
        try:
            image = get_object_or_404(Task_Photo, id=id)
            os.remove(image.image.path)
            image.delete()
            return redirect(request.META['HTTP_REFERER'])
        except:
            return redirect(request.META['HTTP_REFERER'])


class Task_Details(LoginRequiredMixin, View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        return render(request, 'task/task_details.html', {'task': task})
    
    def post(self, request, id):
        task_id = request.POST['task_id']
        task = get_object_or_404(Task, id=task_id)
        
        task_image = request.FILES.get('task_image')
        if not task_image:
            messages.warning(request, 'Image Must Be Set!')
            return redirect(request.META['HTTP_REFERER'])
        
        task_image_add = Task_Photo.objects.create(
            tast=task, image=task_image
        )
        return redirect(request.META['HTTP_REFERER'])

class Task_Complete(LoginRequiredMixin, View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        return render(request, 'task/task_complete.html', {'task': task})
    
    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.task_project_link = request.POST['task_url']
        if request.POST['task_complete_comment']:
            task.task_complete_comment = request.POST['task_complete_comment']
        task.task_complete_user = request.user
        task.is_complete = True
        task.save()
        return redirect('task_details', id=task.id)

@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_complete = True
    task.save()
    return redirect('task_details', id=pk)


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = 'task/task_delete_confirm.html'
    success_url = reverse_lazy('index')
    
    def delete(self, request, *args, **kwargs):
        try:
            task = self.get_object()
            task_image = task.task_photo.all()
            try:
                if task_image:
                    for i in task_image:
                        os.remove(i.image.path)
                        i.delete()
                task.delete()
                return redirect(reverse_lazy('index'))
            except:
                task.delete()
                return redirect(reverse_lazy('index'))
        except:
            return HttpResponse('Some Error')



