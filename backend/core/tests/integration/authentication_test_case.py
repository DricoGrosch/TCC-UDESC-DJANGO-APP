from decouple import config
from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient


class AuthenticationTestCase(TestCase):
    def test_authentication(self):
        client = APIClient()
        response = client.post(reverse_lazy('login'), {
            'username': config('USER_CPF'),
            'password': config('MOODLE_PASSWORD'),
            'device_token':config('DEVICE_TOKEN')
        },format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
