import datetime

from django.conf import settings
from django.db import models
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification


class FavoriteEvent(models.Model):
    event = models.ForeignKey('Event', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def send_notification(self):
        today = datetime.datetime.now()
        user_devices = FCMDevice.objects.filter(active=True, user=self.user)
        for device in user_devices:
            event_date = self.event.date.replace(tzinfo=None)
            if event_date < today:
                continue
            remaining_time_min = (event_date - today).total_seconds() / 60
            remaining_time_hour = remaining_time_min / 60
            message = ''
            if remaining_time_min <= 5:
                message = 'Faltam 5 minutos para sua reunião começar'
            elif remaining_time_hour <= 1:
                message = 'Falta 1 hora para sua reunião começar'
            elif remaining_time_hour <= 24:
                message = f'Faltam {int(remaining_time_hour)} horas para sua reunião começar'
            if message:
                response = device.send_message(
                    Message(notification=Notification(title=f"Lembrete para o evento {self.event.name}", body=message)))
                print(response)
                print('message sent')
