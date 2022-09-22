
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from list_app.models import Task

from datetime import datetime

from list_app.models import Choices



def add_task_view(request):
    if request.method =='GET':
        context = {'choices': Choices.choices}
        return render(request, 'new_task.html', context=context)
    print(request.POST.get('date'))
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'deadline_date': request.POST.get('date')
    }
    task = Task.objects.create(**task_data)
    print('redirect')
    return redirect(f'/')


def display_task_view(request, pk):
    # id = request.GET.get('id')
    # task = Task.objects.get(pk=id)
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponseNotFound("Not Found")
    context = {
        "task": task
    }
    return render(request, 'task.html', context=context)
