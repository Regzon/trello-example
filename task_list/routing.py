from django.urls import path

from task_list.consumers import TaskListConsumer


websocket_urlpatterns = [
    path('ws/task_list/<str:key>/', TaskListConsumer),
]
