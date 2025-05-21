from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages
from django.urls import reverse


def about_view(request):
    """
    Display the About page and handle collaboration form submissions.

    Handles both GET and POST requests:
    - GET: Loads the about content and an empty form.
    - POST: Validates and saves the form if valid, showing a success message.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered About page with context data.
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                (
                    "Collaboration request received! "
                    "I endeavour to respond within 2 working days."
                ),
            )

    about = About.objects.first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        'about/about.html',
        {
            'about': about,
            'collaborate_form': collaborate_form,
            'about_url': reverse('about'),
        },
    )
