from django.db import models
from django.contrib.auth.models import User
from chefs.models import ChefProfile

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
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    favorites = models.ManyToManyField(User, related_name='favorite_recipes', blank=True)
    chef = models.ForeignKey(
        ChefProfile, on_delete=models.CASCADE, related_name="book_recipes"   
    )
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    favorites = models.ManyToManyField(User, related_name='favorite_recipes', blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=0)    
    prep_time = models.CharField(max_length=15,help_text="Preparation time in minutes")
    cook_time = models.CharField(max_length=15,help_text="Cooking time in minutes")
    servings = models.CharField(max_length=15,help_text="Number of servings")
    created_on = models.DateTimeField(auto_now_add=True)

    
    # tags = models.ManyToManyField(Tag, related_name="recipes")
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

class Comment(models.Model):
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
        return f"Comment by {self.author} on {self.recipe}"



# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name

