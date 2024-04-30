from django import forms
from .models import Task

""""
class TaskReportForm(forms.Form):
    start_date = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    priority = forms.ChoiceField(required=False, choices=[('', 'All')] + Task.PRIORITY_CHOICES)
    status = forms.ChoiceField(required=False, choices=[('', 'All')] + Task.STATUS_CHOICES)
    sort = forms.ChoiceField(required=False, choices=[('name', 'Task Name')])
    """


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['due_date', 'status', 'priority', 'user']

