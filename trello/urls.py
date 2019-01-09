from django.urls import path, include

from trello.views import index


urlpatterns = [
    path('', index, name='index'),
    path('task_list/', include('task_list.urls')),
]
