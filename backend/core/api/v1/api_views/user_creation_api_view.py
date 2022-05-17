from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from fcm_django.models import FCMDevice
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.views import APIView

from backend.core.api.v1.serializers.user_serializer import UserSerializer


class UserCreationFromEmailAPIView(APIView):
    def post(self, *args, **kwargs):
        device_token = self.request.data.pop('device_token')
        user = None
        try:
            try:
                user = User.objects.get(username=self.request.data['username'])
                user.first_name = self.request.data['first_name']
                user.last_name = self.request.data['last_name']
            except ObjectDoesNotExist as e:
                serializer = UserSerializer(data=self.request.data, context={'request': self.request})
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
            finally:
                user.set_password(self.request.data['password'])
                user.save()

            token, created = Token.objects.get_or_create(user=user)
            FCMDevice.objects.get_or_create(user=user, registration_id=device_token)
            response_dict = {**UserSerializer(user, context={"request": self.request}).data, 'token': token.key}
            return Response(response_dict, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': 'Credenciais inválidas'}, status=HTTP_401_UNAUTHORIZED)
