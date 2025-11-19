from django import forms
from reservas.models import Scheduling

class SchedulingForm(forms.ModelForm):
    class Meta:
        model = Scheduling
        fields = ['date', 'start', 'end', 'justification']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start': forms.DateInput(attrs={'type': 'time'}),
            'end': forms.DateInput(attrs={'type': 'time'}),
        }