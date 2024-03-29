from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, When, IntegerField
from django.views import View, generic
from django.urls import reverse_lazy
from rest_framework import viewsets
from django.contrib import messages
from .forms import Task_Form
from .serializer import *
from .models import *
import os


class TaskAPI(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = Task_Serializer

class TaskPhotoAPI(viewsets.ModelViewSet):
    queryset = Task_Photo.objects.all()
    serializer_class = TaskPhotoSerializer


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
            task = Task.objects.all().order_by('id')
        
        
        item_per_page = 5
        
        paginator = Paginator(task, item_per_page)
        page = request.GET.get('page')
        try:
            task_list = paginator.page(page)
        except PageNotAnInteger:
            task_list = paginator.page(1)
        except EmptyPage:
            task_list = paginator.page(1)
        except InvalidPage:
            task_list = paginator.page(1)
        
        context['task'] = task_list
        context['paginator'] = paginator
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



