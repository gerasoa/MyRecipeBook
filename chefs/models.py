from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ChefProfile(models.Model):
    """
    Model representing a chef's profile.

    Attributes:
        user (User): The user account associated with this chef profile.
        name (str): The public display name of the chef.
        slug (str): A unique slug for URL usage.
        bio (str): A short biography of the chef.
        photo_small (CloudinaryField): Optional small image for profile
            display.
        photo_large (CloudinaryField): Optional large image for banner or
            detailed views.
        updated_on (datetime): Timestamp of the last update to the profile.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='chef_profile'
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField()
    photo_small = CloudinaryField('photo_small', blank=True, null=True)
    photo_large = CloudinaryField('photo_large', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return the full name of the user for display purposes.
        """
        return self.user.get_full_name()
