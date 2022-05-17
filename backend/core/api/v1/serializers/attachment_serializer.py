from rest_framework.serializers import ModelSerializer

from backend.core.api.v1.serializers.user_serializer import UserSerializer
from backend.core.models import Attachment


class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class AttachmentReadSerializer(ModelSerializer):
    uploaded_by = UserSerializer()

    class Meta:
        model = Attachment
        fields = '__all__'
