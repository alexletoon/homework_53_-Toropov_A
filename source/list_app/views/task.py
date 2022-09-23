
from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseNotFound
from list_app.models import Task

from datetime import datetime

from list_app.models import Choices



def add_task_view(request):
    if request.method =='GET':
        context = {'choices': Choices.choices}
        return render(request, 'new_task.html', context=context)
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'deadline_date': request.POST.get('date')
    }
    task = Task.objects.create(**task_data)
    return redirect(reverse('index_view'))


def display_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        "task": task
    }
    return render(request, 'task.html', context=context)
