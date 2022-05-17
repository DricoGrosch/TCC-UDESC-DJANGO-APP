import binascii
import os
import random

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


class AccountCreationToken(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    key = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    # token is valid only for 5 minutes
    expiration_time_limit = 5

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def use(self):
        self.used = True
        self.save()

    def generate_key(self):
        return random.randint(10000, 99999)

    def is_valid(self):
        in_time_range = ((timezone.now() - self.created_at).total_seconds() / 60) < self.expiration_time_limit
        return in_time_range and not self.used
