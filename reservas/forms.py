from django import forms
from reservas.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["date", "start", "end", "justification"]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "start": forms.DateInput(attrs={"type": "time", "class": "form-control"}),
            "end": forms.DateInput(attrs={"type": "time", "class": "form-control"}),
            "justification": forms.Textarea(attrs={"class": "form-control"}),
        }
