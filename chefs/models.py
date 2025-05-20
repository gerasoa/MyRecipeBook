from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class ChefProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='chef_profile')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField()
    # photo_small = models.ImageField(upload_to='chefs/small/', null=True, blank=True)
    photo_small = CloudinaryField('photo_small', blank=True, null=True)
    # photo_large = models.ImageField(upload_to='chefs/large/', null=True, blank=True)
    photo_large = CloudinaryField('photo_large', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()