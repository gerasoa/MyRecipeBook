from .models import Comment
from django import forms
from .models import Rating


class CommentForm(forms.ModelForm):
    """
    Form for submitting a comment on a recipe.

    Fields:
        body (str): The content of the comment.
    """

    class Meta:
        model = Comment
        fields = ('body',)


class RatingForm(forms.ModelForm):
    """
    Form for submitting a rating score for a recipe.

    Fields:
        score (int): The rating score given by the user.
    """

    class Meta:
        model = Rating
        fields = ['score']
