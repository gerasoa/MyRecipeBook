# from django.urls import reverse # noqa
# from django import forms # noqa
from ..forms import CollaborateForm

from django.test import TestCase # noqa


# Create your tests here.
class AboutFormTest(TestCase):
    def test_form_fields(self):
        form = CollaborateForm()
        self.assertIn('name', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('message', form.fields)

    def test_form_valid_data(self):
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        }
        form = CollaborateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_email(self):
        form_data = {
            'name': 'Test User',
            'email': 'invalid-email',
            'message': 'This is a test message.'
        }
        form = CollaborateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_empty_fields(self):
        form = CollaborateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('message', form.errors)
