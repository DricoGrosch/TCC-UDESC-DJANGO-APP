from django.contrib.auth import get_user_model

from backend.core.api.v1.serializers.user_serializer import UserSerializer
from backend.core.api.v1.viewsets.login_required_model_viewset import LoginRequiredModelViewSet


class UserViewSet(LoginRequiredModelViewSet):
    queryset = get_user_model().objects.order_by('pk')
    serializer_class = UserSerializer


