from django.urls import path
from .views import TaskListCreateRetrieveUpdateDestroyView

urlpatterns = [
    path('tasks/', TaskListCreateRetrieveUpdateDestroyView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskListCreateRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]