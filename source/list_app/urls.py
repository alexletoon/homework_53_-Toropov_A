from django.urls import path

# from list_app import views
from list_app.views.task import add_task_view, display_task_view
from list_app.views.base import index_view


urlpatterns = [
    path("",  index_view, name='index_view'),
    path('task/new_task/', add_task_view, name = 'add_task'),
    path('task/<int:pk>', display_task_view, name='task_view')
]