from django.test import TestCase
from about.models import About, CollaborateRequest # noqa


class AboutModelTestCase(TestCase):
    def setUp(self):
        self.about = About.objects.create(
            title="About the Project",
            content="This is a sample text for the About section."
        )

    def test_str_method(self):
        """Test if the __str__ method returns the title correctly."""
        self.assertEqual(str(self.about), "About the Project")

    def test_content_field(self):
        """Test if the content field was saved correctly."""
        self.assertEqual(self.about.content,
                         "This is a sample text for the About section.")


class CollaborateRequestModelTest(TestCase):
    def setUp(self):
        self.request = CollaborateRequest.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            message="I want to collaborate!"
        )

    def test_str_method(self):
        self.assertEqual(
            str(self.request), "Collaboration request from Jane Doe"
        )

    def test_default_read_value(self):
        self.assertFalse(self.request.read)
