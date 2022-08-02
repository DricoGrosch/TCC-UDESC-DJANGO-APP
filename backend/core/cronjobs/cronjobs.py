import datetime

from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from apscheduler.schedulers.blocking import BlockingScheduler

from backend.core.models import FavoriteEvent, Event

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def send_favorite_events_notifications():
    print('scheduler called')
    for favorite_event in FavoriteEvent.objects.filter(event__date__date__gte=datetime.datetime.now().date()):
        favorite_event.send_notification()