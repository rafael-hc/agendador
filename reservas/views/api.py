from rest_framework import generics

from reservas.models import Reservation, Room
from reservas.serializers import ReservationSerializer, RoomSerializer


class RoomListAPI(generics.ListAPIView):
    queryset = Room.objects.filter(active=True)
    serializer_class = RoomSerializer


class ReservationListCreateAPI(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
