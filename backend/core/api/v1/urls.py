from django.urls import path
from rest_framework.routers import DefaultRouter

from backend.core.api.v1.api_views import *
from backend.core.api.v1.viewsets import *

router = DefaultRouter()

router.register(r'event', EventViewSet)
router.register(r'attachment', AttachmentViewSet)

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    *router.urls,
]
