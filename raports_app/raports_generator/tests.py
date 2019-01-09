from django.test import TestCase
from .models import Report
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User # Required to assign User as a borrower

from django.test.client import Client
# Create your tests here.


class ViewTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')


    def test_basic_3(self):
        a = 1
        assert a == 1

    def test_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

#testing template correction with no permision
    def test_report_nopermision(self):
        response = self.client.get('/raports_generator/reports/', follow = True)
        self.assertEqual(response.status_code, 200)


    def test_create_report_nopermision(self):
        response = self.client.get('/raports_generator/create_report', follow = True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/raports_generator/create_report/')

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


    def test_edit_profile_nopermision(self):
        response = self.client.get('/profile/', follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/profile/')

    def test_password_change_nopermision(self):
        response = self.client.get('/edit_profile/', follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/edit_profile/')

