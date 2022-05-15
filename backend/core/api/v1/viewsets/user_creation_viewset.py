from django.contrib.auth import get_user_model
from django.db import transaction
from fcm_django.models import FCMDevice
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from backend.core.api.v1.serializers.user_serializer import UserSerializer
from backend.core.api.v1.viewsets.login_required_model_viewset import LoginRequiredModelViewSet


class UserCreationViewSet(ModelViewSet):
    queryset = get_user_model().objects.order_by('pk')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                device_token = request.data.pop('device_token')
                response = super(UserCreationViewSet, self).create(request, *args, **kwargs)
                user = request.data['instance']
                token, created = Token.objects.get_or_create(user=user)
                FCMDevice.objects.get_or_create(user=user, registration_id=device_token)
                request.data.update({
                    'token': token.key
                })
                return response
        except:
            return Response({'error': 'Credenciais inválidas'}, status=HTTP_400_BAD_REQUEST)
