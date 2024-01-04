from django.urls import path
from .views import *

urlpatterns = [
    path('task-api-view/', task_api_view.as_view(), name='task_api_view'),
    path('task-api-view/<int:id>/', task_api_view.as_view(), name='task_api_view'),
]