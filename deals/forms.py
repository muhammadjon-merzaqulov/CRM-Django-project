from django import forms
from .models import Deal
import datetime


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ('title', 'contact', 'lead', 'stage', 'amount', 'expected_close_date',
                  'probability', 'description', 'assigned_to')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'expected_close_date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default expected close date to 30 days from now if not provided
        if not self.initial.get('expected_close_date'):
            self.initial['expected_close_date'] = (datetime.date.today() + datetime.timedelta(days=30)).strftime(
                '%Y-%m-%d')