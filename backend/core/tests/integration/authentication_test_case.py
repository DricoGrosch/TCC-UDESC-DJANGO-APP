from decouple import config
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient


class AuthenticationTestCase(TestCase):
    def setUp(self) -> None:
        get_user_model().objects.create_user(username=config('EMAIL_HOST_USER'), password=config('EMAIL_HOST_PASSWORD'))

    def test_authentication(self):
        client = APIClient()
        response = client.post(reverse_lazy('login'), {
            'username': config('EMAIL_HOST_USER'),
            'password': config('EMAIL_HOST_PASSWORD'),
            'device_token': config('DEVICE_TOKEN')
        }, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
