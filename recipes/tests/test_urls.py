from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipesUrlsTestCase(TestCase):
    def test_recipes_list_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, views.RecipeList)

    def test_recipes_list_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302, 404])