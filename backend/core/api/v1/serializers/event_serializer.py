from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.fields import ListField
from rest_framework.serializers import ModelSerializer

from backend.core.api.v1.serializers.attachment_serializer import AttachmentSerializer
from backend.core.api.v1.serializers.user_serializer import UserSerializer
from backend.core.models import Event


class EventDetailSerializer(ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True, source='attachment_set')
    members = UserSerializer(many=True, read_only=True)
    owner = UserSerializer()

    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True, source='attachment_set')
    _members = ListField(default=[])

    class Meta:
        model = Event
        exclude = ['members']

    def set_members(self, members):
        self.instance.members.clear()
        for cnpj in members:
            user, created = get_user_model().objects.get_or_create(username=cnpj)
            if created:
                user.first_name = cnpj
                user.save()
            self.instance.members.add(user)

    def create(self, validated_data):
        try:
            with transaction.atomic():
                members = validated_data.pop('_members')
                self.instance = super(EventSerializer, self).create(validated_data)
                self.set_members(members)
                return self.instance
        except Exception as e:
            print(e)

    def update(self, instance, validated_data):
        try:
            with transaction.atomic():
                members = validated_data.pop('_members')
                self.instance = super(EventSerializer, self).update(instance,validated_data)
                self.set_members(members)
                return self.instance
        except Exception as e:
            print(e)


class EventShortSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'online', 'public', 'favorite']
