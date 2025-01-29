from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField()
    photo = CloudinaryField('image', null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name