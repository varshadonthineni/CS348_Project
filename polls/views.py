from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .forms import TaskForm
from .models import Task
from django.db.models import Avg, Count, Q
from .models import Task, TaskComment, TaskAttachment
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.db import transaction

"""""
@transaction.atomic
def task_report(request):
    tasks = Task.objects.all()
    return render(request, 'task_report_table.html', {'tasks': tasks})
"""""

@transaction.atomic
def task_report(request):
    if request.method == 'GET':
        # Defining SQL query as a prepared statement
        sql = """""
            SELECT name, due_date, status, priority 
            FROM polls_task 
            WHERE due_date BETWEEN %s AND %s 
            AND status = %s 
            AND priority = %s
        """
        # Getting input parameters from the request  
        start_date = request.GET.get('start_date', '2024-01-01')
        end_date = request.GET.get('end_date', '2024-12-31')
        status = request.GET.get('status', 'In Progress')
        priority = request.GET.get('priority', 'High')

        # Execute the prepared statement
        with connection.cursor() as cursor:
            cursor.execute(sql, [start_date, end_date, status, priority])
            rows = cursor.fetchall()

        # Processing the query result
        tasks = []
        for row in rows:
            task = {
                'name': row[0],
                'due_date': row[1],
                'status': row[2],
                'priority': row[3]
            }
            tasks.append(task)

        # Passing the data to the template
        return render(request, 'task_report.html', {'tasks': tasks})



@transaction.atomic
def index(request):
    return render(request, 'base.html')

@transaction.atomic
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

@transaction.atomic
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('polls:task_list')
    return render(request, 'task_form.html', {'form': form})

@transaction.atomic
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('polls:task_list')
    return render(request, 'task_form.html', {'form': form})

@transaction.atomic
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('polls:task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

