from decouple import config
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class AuthenticatedTestCase(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username=config('USER_CPF'),
        )
        self.user.set_password(config('MOODLE_PASSWORD'))
        self.user.save()
        self.client = APIClient()
        self.client.post(reverse_lazy('login'), {
            'username': self.user.username,
            'password': config('MOODLE_PASSWORD'),
            'device_token': config('DEVICE_TOKEN')
        }, format='json')
        token = Token.objects.get(user__username=config('USER_CPF'))
        self.client.login(username=self.user.username, password=config('MOODLE_PASSWORD'))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
