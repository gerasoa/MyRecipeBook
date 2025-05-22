from django.test import TestCase
from .forms import CommentForm, RatingForm

# Create your tests here.


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        """
        Test that the form is valid when given valid data.
        """
        form_data = {
            'body': 'This is a test comment.'
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        """
        Test that the form is invalid when given invalid data.
        """
        form_data = {
            'body': ''
        }
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())


class TestRatingForm(TestCase):
    def test_form_is_valid(self):
        """
        Test that the form is valid when given valid data.
        """
        form_data = {
            'score': 5
        }
        form = RatingForm(data=form_data)
        self.assertTrue(form.is_valid())
