from .models import Comment
from django import forms
from .models import Rating

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']