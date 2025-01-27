from django.db import models

# Create your models here.

# a model for a recipe with a title, description, ingredients, preparation steps, and created_at
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    preparation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# a model 

