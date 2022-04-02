from django.conf import settings
from django.db import models


class Event(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=255)
    public = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    link = models.CharField(max_length=255, null=True, blank=True)
    favorite = models.BooleanField(default=False)
    protocol = models.TextField(null=True, blank=True, verbose_name='ATA')
    guide = models.TextField(null=True, blank=True, verbose_name='Pauta')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)
    all_members_can_edit = models.BooleanField(default=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='member_set')
