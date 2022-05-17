from rest_framework.serializers import ModelSerializer

from backend.core.models import FavoriteEvent


class FavoriteEventSerializer(ModelSerializer):
    class Meta:
        model = FavoriteEvent
        fields = '__all__'
