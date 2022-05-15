from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.core.api.v1.serializers.favorite_event_serializer import FavoriteEventSerializer
from backend.core.models import FavoriteEvent


class MarkAsFavoriteAPIView(APIView):
    def post(self, *args, **kwargs):
        event_id = self.kwargs['event_id']
        user_id = self.request.data['user']
        favorite_event, created = FavoriteEvent.objects.get_or_create(user_id=user_id, event_id=event_id)
        return Response(FavoriteEventSerializer(favorite_event).data,
                        status.HTTP_201_CREATED if created else status.HTTP_200_OK)
