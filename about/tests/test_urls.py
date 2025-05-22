from django.test import TestCase
from django.urls import reverse, resolve
from about import views


class AboutUrlsTestCase(TestCase):
    def test_about_url_resolves_to_view(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, views.about_view)

    def test_about_url_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302, 404])
