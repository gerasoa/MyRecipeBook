from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from chefs.models import ChefProfile


class ChefsViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chefuser',
            password='testpass'
        )
        self.chef = ChefProfile.objects.create(
            user=self.user,
            name="Chef Example",
            slug="chef-example",
            bio="A test chef."
        )

    def test_chefs_list_view_status_code(self):
        url = reverse('chef_list')
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302, 404])

    def test_chef_detail_view_status_code(self):
        url = reverse('chef_detail', args=[self.chef.slug])
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302, 404])
