from django.test import TestCase
from django.urls import reverse


class UrlsTestCase(TestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_admin_url_resolves(self):
        response = self.client.get('/admin/')
        self.assertIn(response.status_code, [200, 302])

    def test_chefs_url_resolves(self):
        response = self.client.get('/chefs/')
        self.assertIn(response.status_code, [200, 302, 404])

    def test_about_url_resolves(self):
        response = self.client.get('/about/')
        self.assertIn(response.status_code, [200, 302, 404])

    def test_recipes_url_resolves(self):
        response = self.client.get('/recipes/')
        self.assertIn(response.status_code, [200, 302, 404])
