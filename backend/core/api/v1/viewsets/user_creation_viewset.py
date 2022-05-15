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