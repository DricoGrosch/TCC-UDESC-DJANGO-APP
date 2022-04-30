from datetime import datetime

from django.urls import reverse_lazy
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from backend.core.models import Event
from backend.core.tests.integration.authenticated_test_case import AuthenticatedTestCase


class EventTestCase(AuthenticatedTestCase):
    def setUp(self):
        super(EventTestCase, self).setUp()
        Event.objects.create(date='2020-01-01 08:00', name='event 1', owner=self.user)
        Event.objects.create(date='2020-01-30 08:00', name='event 2', owner=self.user)
        Event.objects.create(date='2020-02-01', name='event 3', owner=self.user)

    def test_list_events_in_month_range_as_owner(self):
        response = self.client.get(reverse_lazy('event-list'), {
            'year': '2020',
            'month': '01',
        }, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_create_event(self):
        response = self.client.post(reverse_lazy('event-list'), {
            'date': '2020-01-01 08:00', 'name': 'event 1',
        }, format='json')

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertTrue('id' in response.json())
    def test_update_event(self):
        event = Event.objects.get(name='event 1')
        response = self.client.put(reverse_lazy('event-detail', kwargs={'pk': event.id}),{
            'name':'event 1 updated',
            'date':'2020-02-02 08:00'
        })
        self.assertEqual(response.status_code, HTTP_200_OK)
        response_data=response.json()
        self.assertEqual(response_data['name'],'event 1 updated')
        self.assertEqual(response_data['date'],'2020-02-02T08:00:00Z')

