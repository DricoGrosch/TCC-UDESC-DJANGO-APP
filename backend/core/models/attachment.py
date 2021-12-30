from django.db import models


class Attachment(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    file = models.FileField()