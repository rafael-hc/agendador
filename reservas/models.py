from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Room(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name='Nome da Sala/Laboratório'
    )

    capacity = models.IntegerField(verbose_name='Capacidade Máxima de Pessoas')

    type = models.CharField(
        max_length=50,
        choices=[
            ('LAB', 'Laboratório'),
            ('SALA', 'Sala de Aula'),
            ('AUD', 'Auditório'),
        ],
        default='SALA',
        verbose_name='Tipo de Recurso',
    )
    active = models.BooleanField(
        default=True, verbose_name='Disponível para Agendamento'
    )

    def __str__(self):
        return f'{self.name} ({self.capacity} pessoas)'

    class Meta:
        verbose_name = 'Sala Agendável'
        verbose_name_plural = 'Salas Agendáveis'


class Reservation(models.Model):
    # Relacionamento
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='reservations',
        verbose_name='Sala Reservada',
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Solicitante'
    )

    # Dados do agendamento
    date = models.DateField(verbose_name='Data da Reserva')
    start = models.TimeField(verbose_name='Horário de Início')
    end = models.TimeField(verbose_name='Horário de Fim')

    justification = models.TextField(
        blank=True, null=True, verbose_name='Motivo/Justificativa'
    )

    def clean(self):
        if self.end <= self.start:
            raise ValidationError(
                'O horário de término deve ser posterior ao início.'
            )

        conflicting_reservations = Reservation.objects.filter(
            room=self.room,
            date=self.date,
            start__lt=self.end,
            end__gt=self.start,
        )

        if self.id:
            conflicting_reservations = conflicting_reservations.exclude(
                id=self.id
            )

        if conflicting_reservations.exists():
            raise ValidationError('Esta sala já está reservada neste horário.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.room.name} - {self.date} ({self.start} - {self.end})'

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['date', 'start']
