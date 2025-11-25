from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from reservas.forms import ReservationForm
from reservas.models import Reservation, Room


@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == 'POST':
        reservation_temp = Reservation(room=room, user=request.user)
        form = ReservationForm(request.POST, instance=reservation_temp)
        if form.is_valid():
            form.save()

            return redirect('room_details', room_id=room.id)
    else:
        form = ReservationForm()

    return render(
        request, 'reservas/book_room.html', {'form': form, 'room': room}
    )


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by(
        'date'
    )
    return render(
        request, 'reservas/my_reservations.html', {'reservations': reservations}
    )


@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation, pk=reservation_id, user=request.user
    )

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reserva cancelada com sucesso')
        return redirect('my_reservations')

    return render(
        request,
        'reservas/confirm_cancellation.html',
        {'reservation': reservation},
    )
