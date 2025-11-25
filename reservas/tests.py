from datetime import date, time

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Reservation, Room


# Create your tests here.
class ReservationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='tester')

        self.room = Room.objects.create(
            name='Lab test',
            capacity=30,
            type='LAB',
        )

        self.reservation = Reservation.objects.create(
            room=self.room,
            user=self.user,
            date=date(2025, 12, 1),
            start=time(14, 0),
            end=time(16, 0),
        )

    def test_bloqueia_conflito_exato(self):
        with self.assertRaises(ValidationError):
            Reservation.objects.create(
                room=self.room,
                user=self.user,
                date=date(2025, 12, 1),
                start=time(14, 0),
                end=time(16, 0),
            )

    def test_bloqueia_sobreposicao_parcial(self):
        with self.assertRaises(ValidationError):
            Reservation.objects.create(
                room=self.room,
                user=self.user,
                date=date(2025, 12, 1),
                start=time(15, 0),
                end=time(17, 0),
            )

    def test_permite_horario_livre(self):
        reservation_ok = Reservation.objects.create(
            room=self.room,
            user=self.user,
            date=date(2025, 12, 1),
            start=time(16, 0),
            end=time(18, 0),
        )

        try:
            reservation_ok.clean()

        except ValidationError:
            self.fail(
                'O teste falhou: Deveria permitir agendamento sem conflito.'
            )
