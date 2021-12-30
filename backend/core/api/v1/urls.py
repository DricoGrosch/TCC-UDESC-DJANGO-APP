from rest_framework.routers import DefaultRouter

from backend.core.api.v1.viewsets import *

router = DefaultRouter()

router.register(r'event', EventViewSet)
router.register(r'attachment', AttachmentViewSet)

urlpatterns = router.urls
