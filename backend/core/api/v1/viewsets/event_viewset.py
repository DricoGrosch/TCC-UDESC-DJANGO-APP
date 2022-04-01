import datetime

from rest_framework.viewsets import ModelViewSet

from backend.core.api.v1.serializers.event_serializer import EventSerializer, EventShortSerializer, \
    EventDetailSerializer
from backend.core.api.v1.viewsets.login_required_model_viewset import LoginRequiredModelViewSet
from backend.core.models import Event


class EventViewSet(LoginRequiredModelViewSet):
    queryset = Event.objects.order_by('pk')

    def get_serializer_class(self):
        if self.action == 'list':
            return EventShortSerializer
        elif self.action == 'retrieve':
            return EventDetailSerializer
        return EventSerializer

    def get_queryset(self):
        my_private_events = self.request.user.event_set.filter(public=False)
        public_events = Event.objects.filter(public=True)
        return my_private_events | public_events

    def filter_queryset(self, queryset):
        year = self.request.query_params.get('year', '')
        month = self.request.query_params.get('month', '')
        if month:
            queryset = queryset.filter(date__month=month)
        if year:
            queryset = queryset.filter(date__year=year)
        return queryset

    def create(self, request, *args, **kwargs):
        self.request.data['owner'] = self.request.user.id
        return super(EventViewSet, self).create(request, *args, **kwargs)
