from django.conf import settings
from django.core.mail import send_mail
from fcm_django.models import FCMDevice
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK

from backend.core.api.v1.serializers.user_serializer import UserSerializer
from backend.core.models.account_creation_token import AccountCreationToken


class AccountCreationTokenValidationAPIView(ObtainAuthToken):
    def post(self, *args, **kwargs):
        key = self.request.data.pop('token')
        token = AccountCreationToken.objects.get(key=key)
        if not token.is_valid():
            return Response({'error': 'This token has expired'}, status=HTTP_401_UNAUTHORIZED)
        return Response({'ok': True}, status=HTTP_200_OK)
