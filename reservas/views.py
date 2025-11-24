from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from reservas.models import Room, Reservation
from reservas.forms import ReservationForm


def list_rooms(request):
    rooms = Room.objects.filter(active=True)

    return render(request, "reservas/list_rooms.html", {"rooms": rooms})


def room_details(request, room_id):

    room = get_object_or_404(Room, pk=room_id)

    reservations = room.reservation.filter(date__gte=date.today()).order_by(
        "date", "start"
    )

    return render(
        request,
        "reservas/room_details.html",
        {"room": room, "reservations": reservations},
    )


@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == "POST":
        reservation_temp = Reservation(room=room, user=request.user)
        form = ReservationForm(request.POST, instance=reservation_temp)
        if form.is_valid():

            form.save()

            return redirect("room_details", room_id=room.id)
    else:
        form = ReservationForm()

    return render(request, "reservas/book_room.html", {"form": form, "room": room})


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by("date")
    return render(
        request, "reservas/my_reservations.html", {"reservations": reservations}
    )


@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)

    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reserva cancelada com sucesso")
        return redirect("my_reservations")

    return render(
        request, "reservas/confirm_cancellation.html", {"reservation": reservation}
    )
