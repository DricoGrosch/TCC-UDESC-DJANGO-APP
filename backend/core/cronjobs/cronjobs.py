import datetime

from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from apscheduler.schedulers.blocking import BlockingScheduler

from backend.core.models import FavoriteEvent

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def send_favorite_events_notifications():
    print('scheduler called')
    for device in FCMDevice.objects.filter(active=True):
        today = datetime.datetime.now()
        # FavoriteEvent.objects.filter(user=device.user)
        for event in device.user.event_set.filter(favorite=True):
            # o filtro da query é meio zoado pro que eu quero
            event_date = event.date.replace(tzinfo=None)
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
                    Message(notification=Notification(title=f"Lembrete para o evento {event.name}", body=message)))
                print(response)
                print('message sent')
