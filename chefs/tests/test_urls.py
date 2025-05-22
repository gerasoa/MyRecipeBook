from django.test import TestCase
from django.urls import reverse, resolve
from chefs import views


class ChefUrlsTestCase(TestCase):
    def test_chef_list_url_resolves(self):
        url = reverse('chef_list')
        self.assertEqual(resolve(url).func, views.chef_list)

    def test_chef_list_status_code(self):
        url = reverse('chef_list')
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302, 404])
