from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.views import APIView

from backend.core.models.account_creation_token import AccountCreationToken


class AccountCreationRequestTokenAPIView(APIView):
    def post(self, *args, **kwargs):
        email = self.request.data.pop('email')
        if email.split('@')[1] != settings.INTITUTIONAL_EMAIL_SUFIX:
            return Response({'error': 'Email provided is invalid'}, status=HTTP_401_UNAUTHORIZED)
        token = AccountCreationToken.objects.create(email=email).key
        send_mail(f'Token de criação de conta CALENUDESC', f'Este é o token para criação da sua conta {token}',
                  settings.DEFAULT_FROM_EMAIL, [email])
        return Response({'ok': True}, status=HTTP_200_OK)
