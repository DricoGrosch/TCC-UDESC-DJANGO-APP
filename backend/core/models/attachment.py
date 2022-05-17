from django.conf import settings
from django.db import models


class Attachment(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    file = models.FileField()
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)
    upload_date = models.DateField(auto_now_add=True)