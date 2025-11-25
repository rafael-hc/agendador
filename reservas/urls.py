from django.urls import path
from reservas import views

urlpatterns = [
    path("", views.list_rooms, name="list_rooms"),
    path("sala/<int:room_id>/", views.room_details, name="room_details"),
    path("sala/<int:room_id>/reservar/", views.book_room, name="book_room"),
    path("minhas_reservas/", views.my_reservations, name="my_reservations"),
    path(
        "cancelar/<int:reservation_id>/",
        views.cancel_reservation,
        name="cancel_reservation",
    ),
    path("sala/criar/", views.create_room, name="create_room"),
]
