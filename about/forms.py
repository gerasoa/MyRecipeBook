from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    Form for users to submit a collaboration request.

    Fields:
        name (str): The name of the user.
        email (str): The user's email address.
        message (str): The content of the collaboration message.
    """

    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
