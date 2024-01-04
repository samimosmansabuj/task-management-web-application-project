from django.urls import path
from .views import *

urlpatterns = [
    path('', index.as_view(), name='index'),
    
    path('add-task/', TaskCreateView.as_view(), name='add_task'),
    path('update-task/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('task-complete/<int:id>/', Task_Complete.as_view(), name='task_complete'),
    
    path('delete-image/<int:id>/', Delete_Image.as_view(), name='delete_image'),
    path('task/<int:id>/', Task_Details.as_view(), name='task_details'),
    
    
    path('task-api-view/', task_api_view.as_view(), name='task_api_view'),
    path('task-api-view/<int:id>/', task_api_view.as_view(), name='task_api_view'),
]