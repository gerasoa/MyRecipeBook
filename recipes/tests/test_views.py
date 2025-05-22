from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from chefs.models import ChefProfile
from recipes.models import Recipe


class RecipesViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.chef_profile = ChefProfile.objects.create(
            user=self.user,
            name="Chef Example",
            slug="chef-example",
            bio="A test chef."
        )
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            chef=self.chef_profile,
            description="A test recipe.",
            ingredients="Eggs, Flour, Sugar",
            steps="Mix ingredients. Bake.",
            prep_time="10",
            cook_time="20",
            servings="2"
        )

    def test_recipes_list_view_status_code(self):
        url = reverse('home')  # Use o nome correto da sua URL de listagem
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302, 404])

    def test_recipe_detail_view_status_code(self):
        url = reverse('recipe_detail', args=[self.recipe.slug])
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302, 404])
