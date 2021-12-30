from datetime import datetime

from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def send_favorite_events_notifications():
    print('scheduler called')
    for device in FCMDevice.objects.filter(active=True):
        for event in device.user.event_set.filter(favorite=True):
            remaining_time_min = (event.date.replace(tzinfo=None) - datetime.now().replace(
                tzinfo=None)).total_seconds() / 60
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