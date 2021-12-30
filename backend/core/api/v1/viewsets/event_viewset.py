import datetime

from rest_framework.viewsets import ModelViewSet

from backend.core.api.v1.serializers.event_serializer import EventSerializer, EventShortSerializer
from backend.core.models import Event


class EventViewSet(ModelViewSet):
    queryset = Event.objects.order_by('pk')

    def get_serializer_class(self):
        if self.action == 'list':
            return EventShortSerializer
        return EventSerializer

    def get_queryset(self):
        return super(EventViewSet, self).get_queryset().order_by('online')

    def filter_queryset(self, queryset):
        year = self.request.query_params.get('year', '')
        month = self.request.query_params.get('month', '')
        if month:
            queryset = queryset.filter(date__month=month)
        if year:
            queryset = queryset.filter(date__year=year)
        return queryset
