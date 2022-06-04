from django.urls import path
from rest_framework.routers import DefaultRouter

from backend.core.api.v1.api_views import *
from backend.core.api.v1.api_views.account_creation_request_token_api_view import AccountCreationRequestTokenAPIView
from backend.core.api.v1.api_views.account_creation_token_validation_api_view import \
    AccountCreationTokenValidationAPIView
from backend.core.api.v1.api_views.mark_as_favorite_api_view import MarkAsFavoriteAPIView
from backend.core.api.v1.api_views.password_change_api_view import PasswordChangeAPIView
from backend.core.api.v1.api_views.unmark_as_favorite_api_view import UnmarkAsFavoriteAPIView
from backend.core.api.v1.api_views.user_creation_api_view import UserCreationFromEmailAPIView
from backend.core.api.v1.viewsets import *

router = DefaultRouter()

router.register(r'event', EventViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('event/<int:event_id>/mark_favorite/', MarkAsFavoriteAPIView.as_view(), name='mark_as_favorite'),
    path('event/<int:event_id>/unmark_favorite/', UnmarkAsFavoriteAPIView.as_view(), name='unmark_as_favorite'),
    path('account_creation_token/create/', AccountCreationRequestTokenAPIView.as_view(),
         name='get_account_creation_token'),
    path('account_creation_token/validate/', AccountCreationTokenValidationAPIView.as_view(),
         name='check_account_creation_token'),
    path('change_password/', PasswordChangeAPIView.as_view(), name='change_password'),

    path('user_creation_from_email/', UserCreationFromEmailAPIView.as_view(), name='user_creation_from_email'),

    path('event/<int:event_id>/attachment/',
         AttachmentViewSet.as_view({
             'get': 'list',
             'post': 'create',
         }), name='attachment-list'),
    path('event/<int:event_id>/attachment/<int:pk>/',
         AttachmentViewSet.as_view({
             'put': 'update',
             'delete': 'destroy',
         }), name='attachment-detail'),
    *router.urls,
]
