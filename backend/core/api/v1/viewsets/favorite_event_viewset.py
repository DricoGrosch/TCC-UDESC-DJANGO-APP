from rest_framework.viewsets import ModelViewSet

from backend.core.api.v1.serializers.favorite_event_serializer import FavoriteEventSerializer
from backend.core.models import FavoriteEvent


class FavoriteEventViewSet(ModelViewSet):
    queryset = FavoriteEvent.objects.order_by('pk')
    serializer_class = FavoriteEventSerializer
