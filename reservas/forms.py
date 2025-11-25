from django import forms
from reservas.models import Reservation, Room


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

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["name", "capacity", "type", "active"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "capacity": forms.NumberInput(attrs={"class": "form-control"}),
            "type": forms.Select(attrs={"class": "form-control"}),
            "active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }