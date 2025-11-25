from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from reservas.forms import RoomForm
from reservas.models import Room


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'reservas/create_room.html'
    success_url = reverse_lazy('list_rooms')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            from django.core.exceptions import PermissionDenied

            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class RoomListView(ListView):
    model = Room
    template_name = 'reservas/list_rooms.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        queryset = super().get_queryset().filter(active=True)
        query = self.request.GET.get('busca')

        if query:
            if query.isdigit():
                queryset = queryset.filter(capacity__gte=int(query))
            else:
                queryset = queryset.filter(name__icontains=query)

        return queryset


class RoomDetailsView(DetailView):
    model = Room
    template_name = 'reservas/room_details.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = self.object.reservations.filter(
            date__gte=date.today()
        ).order_by('date', 'start')
        return context
