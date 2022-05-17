from django.core.management import BaseCommand

from backend.core.cronjobs.cronjobs import sched


class Command(BaseCommand):
    def handle(self, *args, **options):
        sched.start()