from django.conf import settings
from django.core.mail import send_mail
from fcm_django.models import FCMDevice
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK

from backend.core.api.v1.serializers.user_serializer import UserSerializer
from backend.core.models.account_creation_token import AccountCreationToken


class AccountCreationRequestTokenAPIView(ObtainAuthToken):
    def post(self, *args, **kwargs):
        email = self.request.data.pop('email')
        token = AccountCreationToken.objects.create().key
        send_mail(f'Token de criação de conta CALENUDESC', f'Este é o token para criação da sua conta {token}',
                  settings.DEFAULT_FROM_EMAIL, [email])
        return Response({'ok':True}, status=HTTP_200_OK)
