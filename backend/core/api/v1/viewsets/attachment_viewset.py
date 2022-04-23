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
        image_extensions = ['jpeg',
                            'jpg',
                            'png',
                            'gif',
                            'tiff',
                            'psd',
                            'eps',
                            'ai',
                            'indd', ]
        if self.kwargs.get('event_id'):
            queryset = queryset.filter(event_id=self.kwargs['event_id'])
        if 'only_files' in self.request.query_params:
            _qs = queryset
            for attachment in _qs:
                file_extensions = attachment.file.name.split('.')[-1]
                if file_extensions in image_extensions:
                    queryset = queryset.exclude(id=attachment.id)
        if 'only_images' in self.request.query_params:
            _qs = queryset
            for attachment in _qs:
                file_extensions = attachment.file.name.split('.')[-1]
                if file_extensions not in image_extensions:
                    queryset = queryset.exclude(id=attachment.id)
        return queryset

    def create(self, request, *args, **kwargs):
        self.request.data['uploaded_by'] = self.request.user.id
        self.request.data['event'] = self.kwargs['event_id']
        return super(AttachmentViewSet, self).create(request, *args, **kwargs)
