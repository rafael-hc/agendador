from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers

from .models import Reservation, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'capacity', 'type', 'active']


class ReservationSerializer(serializers.ModelSerializer):
    room_name = serializers.ReadOnlyField(source='room.name')

    class Meta:
        model = Reservation
        fields = [
            'id',
            'room',
            'room_name',
            'user',
            'date',
            'start_time',
            'end_time',
        ]

    def validate(self, data):
        instance = self.instance

        temp_reservation = Reservation(**data)

        if instance:
            temp_reservation.id = instance.id

        try:
            temp_reservation.clean()
        except DjangoValidationError as e:
            if hasattr(e, 'error_dict'):
                raise serializers.ValidationError(e.message_dict)
            else:
                raise serializers.ValidationError(
                    {'non_field_errors': e.messages}
                )
        return
