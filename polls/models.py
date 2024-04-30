from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime



class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('I', 'In Progress'),
        ('O', 'On Hold'),
    ]
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    completed_at = models.DateTimeField(null=True, blank=True)  # This line is added
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
        return self.name

class TaskComment(models.Model):
    comment = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.name}'

class TaskAttachment(models.Model):
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')


class Indexes:
        indexes = [
            models.Index(fields=['due_date'], name='task_due_date_idx'),
            models.Index(fields=['status'], name='task_status_idx'),
            models.Index(fields=['priority'], name='task_priority_idx'),
            models.Index(fields=['due_date', 'status'], name='task_due_date_status_idx'),
        ]

def __str__(self):
    return self.file_name

