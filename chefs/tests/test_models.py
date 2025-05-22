from django.test import TestCase
from django.contrib.auth.models import User
from chefs.models import ChefProfile


class ChefProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chefuser',
            password='testpass',
            first_name='Chef',
            last_name='Example'
        )
        self.chef = ChefProfile.objects.create(
            user=self.user,
            name="Chef Example",
            slug="chef-example",
            bio="A test chef."
        )

    def test_str_method(self):
        self.assertEqual(str(self.chef), "Chef Example")

    def test_bio_field(self):
        self.assertEqual(self.chef.bio, "A test chef.")
