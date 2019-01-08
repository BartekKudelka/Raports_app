from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class ViewsTest(TestCase):

    def test_view_url_login_exists_at_desired_location(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_sign_up_url_exists_at_desired_location(self):
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_login_accessible_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_view_sign_up_url_accessible_by_name(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)


class LogInTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'filip',
            'password': 'zaq1@WSX'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
