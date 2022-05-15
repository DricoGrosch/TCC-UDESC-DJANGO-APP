from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.core.api.v1.serializers.event_serializer import EventDetailSerializer
from backend.core.models import FavoriteEvent, Event


class UnmarkAsFavoriteAPIView(APIView):
    def post(self, *args, **kwargs):
        event_id = self.kwargs['event_id']
        user_id = self.request.data['user']
        FavoriteEvent.objects.get(user_id=user_id, event_id=event_id).delete()
        return Response(EventDetailSerializer(Event.objects.get(id=event_id)).data, status.HTTP_200_OK)
