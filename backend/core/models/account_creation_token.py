import binascii
import os
import random

from django.conf import settings
from django.db import models


class AccountCreationToken(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    key = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return random.randint(10000, 99999)

    def is_valid(self):
        # todo
        return True
