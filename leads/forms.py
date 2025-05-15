from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('contact', 'title', 'description', 'status', 'priority', 'estimated_value', 'assigned_to')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'estimated_value': forms.NumberInput(attrs={'step': '0.01'}),
        }