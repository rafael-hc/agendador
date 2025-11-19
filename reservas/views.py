from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from reservas.models import Room, Scheduling
from reservas.forms import SchedulingForm

def list_rooms(request):
    rooms = Room.objects.filter(active=True)

    return render(request, 'reservas/list_rooms.html', {'rooms': rooms})

def room_details(request, room_id):

    room = get_object_or_404(Room, pk=room_id)

    scheduling = room.scheduling.filter(
        date__gte=date.today()
    ).order_by('date', 'start')

    return render(request, 'reservas/room_details.html', {
        'room': room,
        'scheduling': scheduling
    })

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == 'POST':
        schedule_temp = Scheduling(room=room, user=request.user)
        form = SchedulingForm(request.POST, instance=schedule_temp)
        if form.is_valid():
            
            form.save()

            return redirect('room_details', room_id=room.id)
    else:
        form = SchedulingForm()

    return render(request, 'reservas/book_room.html', {
        'form': form,
        'room': room
    })