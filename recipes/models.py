from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.

# a model for a recipe with a title, description, ingredients, preparation steps, and created_at
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    #slug = models.SlugField(max_length=200, unique=True)
    slug = models.SlugField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_recipes"   
    )
    ingredients = models.TextField()
    steps = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # tags = models.ManyToManyField(Tag, related_name="recipes")
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     recipe = models.ForeignKey(
#         Recipe, on_delete=models.CASCADE, related_name="comments")
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="commenter")
#     body = models.TextField()
#     approved = models.BooleanField(default=False)
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-created_on"]

#     def __str__(self):
#         return self.title



# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name

