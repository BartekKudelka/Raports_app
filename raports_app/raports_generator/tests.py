from django.test import TestCase
from .models import Report
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate


class ViewsTest(TestCase):

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



    def test_visual_report_with_permision(self):
        response = self.client.get('/raports_generator/show_visual_report/1/', follow=True)
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('create_report'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"


        self.assertEqual(response.status_code, 200)
        user = authenticate(username='admin2', password='zaq1@WSX')
        print(user)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/raports_generator/show_visual_report/1/')