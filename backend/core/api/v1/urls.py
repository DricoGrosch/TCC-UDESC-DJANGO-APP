from django.urls import path
from rest_framework.routers import DefaultRouter

from backend.core.api.v1.api_views import *
from backend.core.api.v1.api_views.mark_as_favorite_api_view import MarkAsFavoriteAPIView
from backend.core.api.v1.api_views.unmark_as_favorite_api_view import UnmarkAsFavoriteAPIView
from backend.core.api.v1.viewsets import *

router = DefaultRouter()

router.register(r'event', EventViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('login/', LoginAPIView.as_view(),name='login'),
    path('event/<int:event_id>/mark_favorite/', MarkAsFavoriteAPIView.as_view(),name='mark_as_favorite'),
    path('event/<int:event_id>/unmark_favorite/', UnmarkAsFavoriteAPIView.as_view(),name='unmark_as_favorite'),

    path('event/<int:event_id>/attachment/',
         AttachmentViewSet.as_view({
             'get': 'list',
             'post': 'create',
         }),name='attachment-list'),
    path('event/<int:event_id>/attachment/<int:pk>/',
         AttachmentViewSet.as_view({
             'put': 'update',
             'delete': 'destroy',
         }),name='attachment-detail'),
    *router.urls,
]
