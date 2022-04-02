from backend.core.api.v1.serializers.attachment_serializer import AttachmentSerializer, AttachmentReadSerializer
from backend.core.api.v1.viewsets.login_required_model_viewset import LoginRequiredModelViewSet
from backend.core.models import Attachment


class AttachmentViewSet(LoginRequiredModelViewSet):
    queryset = Attachment.objects.order_by('pk')

    def get_serializer_class(self):
        if self.action == 'list':
            return AttachmentReadSerializer
        return AttachmentSerializer

    def filter_queryset(self, queryset):
        if self.kwargs.get('pk'):
            return queryset.filter(event_id=self.kwargs['pk'])
        return queryset

    def create(self, request, *args, **kwargs):
        self.request.data['uploaded_by'] = self.request.user.id
        self.request.data['event'] = self.kwargs['pk']
        return super(AttachmentViewSet, self).create(request, *args, **kwargs)
