from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from fcm_django.models import FCMDevice
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.views import APIView

from backend.core.api.v1.serializers.user_serializer import UserSerializer
from backend.core.models.account_creation_token import AccountCreationToken


class AccountCreationTokenValidationAPIView(APIView):
    def post(self, *args, **kwargs):
        response = None
        try:
            key = self.request.data['token']
            token = AccountCreationToken.objects.get(key=key)
            if not token.is_valid():
                raise Exception('Token invalid')
            token.use()
            response = Response({'ok': True}, status=HTTP_200_OK)

        except:
            response = Response({'error': 'Token invalid'}, status=HTTP_401_UNAUTHORIZED)
        finally:
            return response
