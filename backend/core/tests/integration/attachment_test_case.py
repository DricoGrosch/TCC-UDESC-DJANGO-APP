import os
from datetime import datetime

from django.conf import settings
from django.urls import reverse_lazy
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from backend.core.models import Event, FavoriteEvent, Attachment
from backend.core.tests.integration.authenticated_test_case import AuthenticatedTestCase


class AttachmentTestCase(AuthenticatedTestCase):
    def setUp(self):
        super(AttachmentTestCase, self).setUp()
        self.event = Event.objects.create(date='2020-01-01 08:00', name='event 1', owner=self.user)
        Attachment.objects.create(file=os.path.join(settings.MEDIA_ROOT, 'test_image.jpg'), uploaded_by=self.user,
                                  event=self.event)
        Attachment.objects.create(file=os.path.join(settings.MEDIA_ROOT, 'test_file.pdf'), uploaded_by=self.user,
                                  event=self.event)

    def test_list_only_images(self):
        response = self.client.get(reverse_lazy('attachment-list', kwargs={'event_id': self.event.id}), {
            'only_images': True,
        }, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_list_only_files(self):
        response = self.client.get(reverse_lazy('attachment-list', kwargs={'event_id': self.event.id}), {
            'only_files': True,
        }, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
