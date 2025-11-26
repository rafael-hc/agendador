# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from reservas import views

urlpatterns = [
    path('', views.RoomListView.as_view(), name='list_rooms'),
    path(
        'sala/<int:pk>/',
        views.RoomDetailsView.as_view(),
        name='room_details',
    ),
    path(
        'sala/<int:room_id>/reservar/',
        views.ReservationCreateView.as_view(),
        name='reserve_room',
    ),
    path(
        'minhas_reservas/',
        views.MyReservationsListView.as_view(),
        name='my_reservations',
    ),
    path(
        'cancelar/<int:pk>/',
        views.ReservationDeleteView.as_view(),
        name='cancel_reservation',
    ),
    path('sala/criar/', views.RoomCreateView.as_view(), name='create_room'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
