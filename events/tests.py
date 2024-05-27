# from django.test import TestCase

# Create your tests here.


# events/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event, Booking

class EventModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.event = Event.objects.create(
            title='Test Event',
            description='Event Description',
            date='2024-06-01 10:00:00',
            location='Test Location',
            organizer=self.user
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.organizer.username, 'testuser')
