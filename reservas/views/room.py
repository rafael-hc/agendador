from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from reservas.forms import RoomForm
from reservas.models import Room


def is_admin(user):
    return user.is_staff


@login_required
@user_passes_test(is_admin)
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sala cadastrada com sucesso.')
            return redirect('list_rooms')
    else:
        form = RoomForm()

    return render(request, 'reservas/create_room.html', {'form': form})


def list_rooms(request):
    rooms = Room.objects.filter(active=True)

    query = request.GET.get('busca')

    if query:
        if query.isdigit():
            rooms = rooms.filter(capacity__gte=int(query))
        else:
            rooms = rooms.filter(name__icontains=query)

    return render(request, 'reservas/list_rooms.html', {'rooms': rooms})


def room_details(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    reservations = room.reservation.filter(date__gte=date.today()).order_by(
        'date', 'start'
    )

    return render(
        request,
        'reservas/room_details.html',
        {'room': room, 'reservations': reservations},
    )
