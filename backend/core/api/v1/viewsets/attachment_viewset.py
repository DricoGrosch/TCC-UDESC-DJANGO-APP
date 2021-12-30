from rest_framework.viewsets import ModelViewSet

from backend.core.api.v1.serializers.attachment_serializer import AttachmentSerializer
from backend.core.models import Attachment


class AttachmentViewSet(ModelViewSet):
    queryset = Attachment.objects.order_by('pk')
    serializer_class = AttachmentSerializer
