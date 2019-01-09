import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'task_list/index.html')


def room(request, key):
    return render(request, 'task_list/room.html', {
        'access_key': mark_safe(json.dumps(key)),
    })
