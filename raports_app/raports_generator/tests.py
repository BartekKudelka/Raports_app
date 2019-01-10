from django.test import TestCase


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

    def test_visit_profile_nopermision(self):
        response = self.client.get('/profile/', follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/profile/')

    def test_edit_profile_nopermision(self):
        response = self.client.get('/edit_profile/', follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/edit_profile/')

    def test_password_change_nopermision(self):
        response = self.client.get('/password/', follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(status_code, 302)
        self.assertEqual(last_url, '/login/?next=/password/')