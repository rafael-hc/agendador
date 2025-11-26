from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from reservas.forms import ReservationForm
from reservas.models import Reservation, Room


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservas/reserve_room.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        if 'room_id' in self.kwargs:
            self.room = get_object_or_404(Room, pk=self.kwargs['room_id'])

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance.room = self.room
        form.instance.user = self.request.user
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = self.room
        return context

    def get_success_url(self):
        return reverse_lazy('room_details', kwargs={'pk': self.room.pk})


class MyReservationsListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservas/my_reservations.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user).order_by(
            'date', 'start'
        )


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'reservas/confirm_cancellation.html'
    context_object_name = 'reservation'
    success_url = reverse_lazy('my_reservations')

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
