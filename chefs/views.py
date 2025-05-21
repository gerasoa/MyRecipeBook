from django.shortcuts import render, get_object_or_404
from .models import ChefProfile
from django.urls import reverse
from recipes.models import Recipe
from django.db.models import Count


def chef_list(request):
    """
    Display a list of all chef profiles.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered page showing all chefs.
    """
    chefs = ChefProfile.objects.all()
    return render(
        request,
        'chefs/chef_list.html',
        {
            'chefs': chefs,
            'chef_url': reverse('chef_list')
        }
    )


def chef_detail(request, slug):
    """
    Display the details of a specific chef and their recipes.

    Retrieves a chef profile based on the slug and lists their associated
    recipes, along with the number of comments on each.

    Args:
        request (HttpRequest): The incoming HTTP request.
        slug (str): The slug of the chef to display.

    Returns:
        HttpResponse: The rendered page with the chef's profile and recipes.
    """
    chef = get_object_or_404(ChefProfile, slug=slug)
    recipes = (
        Recipe.objects.filter(chef=chef)
        .annotate(comment_count=Count('comments'))
    )
    return render(
        request,
        'chefs/chef_detail.html',
        {'chef': chef, 'recipes': recipes}
    )
