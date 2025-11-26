from django import forms

from reservas.models import Reservation, Room


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'start_time', 'end_time', 'justification']

        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'start_time': forms.DateInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'end_time': forms.DateInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'justification': forms.Textarea(attrs={'class': 'form-control'}),
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'type', 'active']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
