from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.core.api.v1.serializers.favorite_event_serializer import FavoriteEventSerializer
from backend.core.models import FavoriteEvent


class LoginRequiredAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
