from django.conf import settings
from django.db import models


class FavoriteEvent(models.Model):
    event = models.ForeignKey('Event', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
