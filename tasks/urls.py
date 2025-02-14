from django.urls import path
from .views import signin, signup, tasks, create_task, task_detail, complete_task, delete_task, signout

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('tasks/', tasks, name='tasks'),
    path('create_task/', create_task, name='create_task'),
    path('task_detail/<int:task_id>/', task_detail, name='task_detail'),
    path('complete_task/<int:task_id>/', complete_task, name='complete_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('signout/', signout, name='signout'),
] 