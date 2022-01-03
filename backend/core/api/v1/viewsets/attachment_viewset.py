from backend.core.api.v1.serializers.attachment_serializer import AttachmentSerializer
from backend.core.api.v1.viewsets.login_required_model_viewset import LoginRequiredModelViewSet
from backend.core.models import Attachment


class AttachmentViewSet(LoginRequiredModelViewSet):
    queryset = Attachment.objects.order_by('pk')
    serializer_class = AttachmentSerializer
