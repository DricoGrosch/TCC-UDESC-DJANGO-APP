from django.urls import path
from rest_framework.routers import DefaultRouter

from backend.core.api.v1.api_views import *
from backend.core.api.v1.viewsets import *

router = DefaultRouter()

router.register(r'event', EventViewSet)

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('event/<int:pk>/attachment/',
         AttachmentViewSet.as_view({
             'get': 'list',
             'put': 'update',
             'post': 'create',
             'delete': 'destroy'
         })),
    *router.urls,
]
