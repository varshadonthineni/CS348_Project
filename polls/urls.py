from django.urls import path
from . import views
from .views import task_report


app_name = 'polls'  

urlpatterns = [
    path("", views.index, name="index"),
    #path('<int:task_id>/', views.task_detail, name='task_detail'),
    #path('<int:task_id>/results/', views.task_results, name='task_results'),
    #path('<int:task_id>/update_status/', views.task_update_status, name='update_status'),
    path('task_report/', views.task_report, name='task_report'),
    path('task_list/', views.task_list, name='task_list'),
    path('task_create/', views.task_create, name='task_create'),
    path('task_update/<int:pk>/', views.task_update, name='task_update'),
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete'),
]
