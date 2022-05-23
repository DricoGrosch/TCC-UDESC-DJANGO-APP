import datetime
import os

from django.conf import settings
from django.core.files import File
from django.test import TestCase

from backend.core.models import Attachment, Event


class AttachmentTestCase(TestCase):

    def setUp(self) -> None:
        event = Event.objects.create(name='test', date=datetime.datetime.now())
        media_path = os.path.join(settings.BASE_DIR, 'backend', 'core', 'tests', 'test_media')
        self.image = Attachment(event=event)
        self.image.file.save('image.jpg', File(open(os.path.join(media_path, 'image.jpg'), 'rb')))
        self.file = Attachment(event=event)
        self.file.file.save('image.pdf', File(open(os.path.join(media_path, 'file.pdf'), 'rb')))

    def test_check_file_is_image(self):
        self.assertTrue(self.image.is_image())

    def test_check_file_is_not_image(self):
        self.assertFalse(self.file.is_image())
