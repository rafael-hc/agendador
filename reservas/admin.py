from django.contrib import admin

from reservas.models import Reservation, Room


@admin.register(Room)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'type', 'active')
    search_fields = ('name',)
    list_filter = ('type', 'active')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'date', 'start_time', 'end_time')
    list_filter = ('date', 'room')
