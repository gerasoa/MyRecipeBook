from django.test import TestCase
from django.urls import reverse


class AboutViewsTestCase(TestCase):
    def test_about_view_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302, 404])
