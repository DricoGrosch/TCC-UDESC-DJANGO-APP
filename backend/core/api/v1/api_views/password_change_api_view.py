from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.views import APIView

from backend.core.api.v1.api_views.login_required_api_view import LoginRequiredAPIView
from backend.core.api.v1.serializers.user_serializer import UserSerializer
from backend.core.models.account_creation_token import AccountCreationToken


class PasswordChangeAPIView(LoginRequiredAPIView):
    def post(self, *args, **kwargs):
        password = self.request.data.pop('password')
        self.request.user.set_password(password)
        self.request.user.save()
        serializer = UserSerializer(self.request.user, context={'request': self.request})
        return Response(serializer.data, status=HTTP_200_OK)

