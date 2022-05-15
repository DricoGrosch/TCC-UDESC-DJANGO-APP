from fcm_django.models import FCMDevice
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK

from backend.core.api.v1.serializers.user_serializer import UserSerializer


class LoginAPIView(ObtainAuthToken):
    def post(self, *args, **kwargs):
        device_token = self.request.data.pop('device_token')
        try:
            serializer = self.serializer_class(data=self.request.data, context={'request': self.request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token= Token.objects.get(user=user)
            FCMDevice.objects.get_or_create(user=user, registration_id=device_token)
            response_dict ={**UserSerializer(user, context={"request": self.request}).data, 'token': token.key}
            return Response(response_dict,status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': 'Credenciais inválidas'}, status=HTTP_401_UNAUTHORIZED)
