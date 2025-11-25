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
    path('sala/<int:room_id>/reservar/', views.book_room, name='book_room'),
    path('minhas_reservas/', views.my_reservations, name='my_reservations'),
    path(
        'cancelar/<int:reservation_id>/',
        views.cancel_reservation,
        name='cancel_reservation',
    ),
    path('sala/criar/', views.RoomCreateView.as_view(), name='create_room'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
