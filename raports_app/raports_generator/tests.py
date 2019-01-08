from django.test import TestCase
from .models import Report
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate


class ViewsTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_report_nopermision(self):
        response = self.client.get('/raports_generator/reports/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create_report_nopermision(self):
        response = self.client.get('/raports_generator/reports/', follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/raports_generator/reports/')

    def test_edit_report_nopermision(self):
        response = self.client.get('/raports_generator/edit_report/1/', follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/raports_generator/edit_report/1/')

    def test_text_report_nopermision(self):
        response = self.client.get('/raports_generator/show_text_report/1/', follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/raports_generator/show_text_report/1/')

    def test_visual_report_nopermision(self):
        response = self.client.get('/raports_generator/show_visual_report/1/', follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/raports_generator/show_visual_report/1/')

