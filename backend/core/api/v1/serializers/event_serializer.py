from rest_framework.serializers import ModelSerializer

from backend.core.api.v1.serializers.attachment_serializer import AttachmentSerializer
from backend.core.models import Event


class EventSerializer(ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True, source='attachment_set')

    class Meta:
        model = Event
        fields = '__all__'


class EventShortSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'online', 'public', 'favorite']
