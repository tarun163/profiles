from django.test import TestCase
from django.urls import reverse
from users.models import User
from rest_framework import status
from rest_framework.test import APIClient, force_authenticate
from profiles.models import Profile

class ProfileAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('profile-create-update')
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.valid_payload = {
            'name': 'tarun kumar',
            'email': 'tarunkumar@gmail.com',
            'bio': 'backend developer',
        }

    def test_create_profile(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get().name, 'tarun kumar')

    def test_update_profile(self):
        self.client.force_authenticate(user=self.user)
        profile = Profile.objects.create(name='tarun kumar', email='tarunkumar@gmail.com', user=self.user)
        payload = {
            'bio': 'backend developer',
        }
        response = self.client.patch(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        profile.refresh_from_db()
        self.assertEqual(profile.bio, 'backend developer')
