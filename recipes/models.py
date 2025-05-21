from django.db import models
from django.contrib.auth.models import User
from chefs.models import ChefProfile
# from django import forms
# from .models import Rating
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

DIFFICULTY = (
    (0, "Easy"),
    (1, "Medium"),
    (2, "Hard"),
)


# Create your models here.
class Recipe(models.Model):
    """
    Model representing a recipe posted by a chef.

    Attributes:
        title (str): The title of the recipe.
        slug (str): URL-friendly version of the title.
        photo (CloudinaryField): Optional image for the recipe.
        chef (ChefProfile): The chef who created the recipe.
        description (str): A short summary of the recipe.
        ingredients (str): Ingredients required for the recipe.
        steps (str): Preparation steps for the recipe.
        status (int): Whether the recipe is a draft or published.
        average_rating (float): Average user rating.
        favorites (ManyToMany[User]): Users who favourited this recipe.
        difficulty (int): Difficulty level (easy, medium, hard).
        prep_time (str): Time required to prepare the ingredients.
        cook_time (str): Time required to cook the recipe.
        servings (str): Number of servings.
        created_on (datetime): Date and time the recipe was created.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    photo = CloudinaryField('image', null=True, blank=True)
    favorites = models.ManyToManyField(
        User, related_name='favorite_recipes', blank=True
    )
    chef = models.ForeignKey(
        ChefProfile, on_delete=models.CASCADE, related_name="book_recipes"
    )
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    average_rating = models.FloatField(default=0.0)
    favorites = models.ManyToManyField(
        User,
        related_name='favorite_recipes',
        blank=True
    )
    difficulty = models.IntegerField(choices=DIFFICULTY, default=0)
    prep_time = models.CharField(
        max_length=15,
        help_text="Preparation time in minutes"
    )
    cook_time = models.CharField(
        max_length=15,
        help_text="Cooking time in minutes"
    )
    servings = models.CharField(max_length=15, help_text="Number of servings")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model representing a comment on a recipe.

    Attributes:
        recipe (Recipe): The recipe the comment is related to.
        author (User): The user who wrote the comment.
        body (str): The comment content.
        approved (bool): Whether the comment is approved for display.
        created_on (datetime): Timestamp when the comment was created.
    """

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        Return a string representation of the comment.
        """

        return f"Comment by {self.author} on {self.recipe}"


class Rating(models.Model):
    """
    Model representing a user-submitted rating for a recipe.

    Attributes:
        recipe (Recipe): The rated recipe.
        user (User): The user who submitted the rating.
        score (int): Rating score given by the user.
        created_on (datetime): Timestamp when the rating was created.

    Meta:
        unique_together: Ensures a user can rate a recipe only once.
    """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'user')
