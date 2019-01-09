from django.urls import path

from task_list.views import index, room


app_name = 'task_list'

urlpatterns = [
    path('', index, name='index'),
    path('<str:key>/', room, name='room'),
]
