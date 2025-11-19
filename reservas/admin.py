from django.contrib import admin

from reservas.models import Room, Scheduling

@admin.register(Room)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'type', 'active')
    search_fields = ('name',)
    list_filter =  ('type', 'active')

@admin.register(Scheduling)
class SchedulingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'date', 'start', 'end')
    list_filter = ('date', 'room')