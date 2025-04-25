from django.urls import path
from .views import task_toggle_complete, TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskReorder

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    path('toggle-complete/<int:id>/', task_toggle_complete, name='task-toggle-complete'),
    
]