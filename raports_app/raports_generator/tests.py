from django.test import TestCase
from .models import Report
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User # Required to assign User as a borrower
# Create your tests here.


class ViewTest(TestCase):

    # def setUp(self):
    #     # Create report
    #     test_report = Report.addReport(self)


    def test_basic_3(self):
        a = 1
        assert a == 1

    def test_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

#testing template correction with no permision
    def test_report_nopermision(self):
        response = self.client.get(reverse('reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports.html')

    def test_create_report_nopermision(self):
        response = self.client.get(reverse('create_report'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_report.html')

    def test_edit_report_nopermision(self):
        response = self.client.get('/edit_report/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_report.html')

    def test_text_report_nopermision(self):
        response = self.client.get('/show_text_report/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'text_report.html')

    def test_visual_report_nopermision(self):
        response = self.client.get('/show_visual_report/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'visual_report.html/1/')


    def test_edit_profile_nopermision(self):
        response = self.client.get('/edit_profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_profile.html')

    def test_password_change_nopermision(self):
        response = self.client.get('/change_password/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'password_change.html')

    def setUp(self):
        # Create user
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_reports_logged(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('reports'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'reports.html')


    def test_create_reports_logged(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('create_report'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'create_report.html')


    def test_edit_reports_logged(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('edit_report'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'edit_report.html')

    def test_text_report_logged(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('show_text_report'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'text_report.html')


    def test_visual_report_logged(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('show_visual_report'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'visual_report.html')


    def test_edit_profile_logged(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('edit_profile'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'edit_profile.html')


    def test_password_change_logged(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('change_password'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'password_change.html')