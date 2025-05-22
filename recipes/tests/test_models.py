from django.test import TestCase
from django.contrib.auth.models import User
from chefs.models import ChefProfile
from recipes.models import Recipe, Comment, Rating


class RecipeModelTestCase(TestCase):
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

    def test_str_method(self):
        self.assertEqual(str(self.recipe), "Test Recipe")


class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='commenter',
            password='testpass'
        )
        self.chef_profile = ChefProfile.objects.create(
            user=self.user,
            name="Chef Commenter",
            slug="chef-commenter",
            bio="Bio"
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
        self.comment = Comment.objects.create(
            recipe=self.recipe,
            author=self.user,
            body="Nice recipe!"
        )

    def test_str_method(self):
        self.assertEqual(
            str(self.comment),
            f"Comment by {self.user} on {self.recipe}"
        )


class RatingModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='rater',
            password='testpass'
        )
        self.chef_profile = ChefProfile.objects.create(
            user=self.user,
            name="Chef Rater",
            slug="chef-rater",
            bio="Bio"
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
        self.rating = Rating.objects.create(
            recipe=self.recipe,
            user=self.user,
            score=5
        )

    def test_score_field(self):
        self.assertEqual(self.rating.score, 5)
