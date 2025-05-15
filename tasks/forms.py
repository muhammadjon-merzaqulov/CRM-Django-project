from django import forms
from .models import Task
import datetime


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'priority', 'due_date',
                  'contact', 'lead', 'deal', 'assigned_to')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Convert due_date to the format expected by datetime-local input
        if self.instance.pk and self.instance.due_date:
            self.initial['due_date'] = self.instance.due_date.strftime('%Y-%m-%dT%H:%M')
        elif not self.initial.get('due_date'):
            # Set default due date to tomorrow at 9 AM if not provided
            tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
            tomorrow = tomorrow.replace(hour=9, minute=0, second=0, microsecond=0)
            self.initial['due_date'] = tomorrow.strftime('%Y-%m-%dT%H:%M')