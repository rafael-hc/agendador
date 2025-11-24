from datetime import date
from django.shortcuts import get_object_or_404, render
from reservas.models import Room


def list_rooms(request):
    rooms = Room.objects.filter(active=True)

    query = request.GET.get("busca")

    if query:
        if query.isdigit():
            rooms = rooms.filter(capacity__gte=int(query))
        else:
            rooms = rooms.filter(name__icontains=query)

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
