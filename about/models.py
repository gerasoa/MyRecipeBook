from django.db import models


class About(models.Model):
    """
    Model representing the content of the About page.

    Attributes:
        title (str): The title of the about section.
        content (str): The main text content.
        update_on (datetime): Timestamp of the last update.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return the title as the string representation of the object.
        """
        return self.title


class CollaborateRequest(models.Model):
    """
    Model for storing collaboration requests submitted via the form.

    Attributes:
        name (str): The name of the person requesting collaboration.
        email (str): Contact email.
        message (str): The message sent in the request.
        read (bool): Whether the request has been marked as read.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """
        Return a readable identifier for the collaboration request.
        """
        return f"Collaboration request from {self.name}"
