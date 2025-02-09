from django.shortcuts import render, get_object_or_404
from .models import ChefProfile
from django.urls import reverse
from recipes.models import Recipe

def chef_list(request):
    chefs = ChefProfile.objects.all()
    return render(request, 'chefs/chef_list.html', {'chefs': chefs, 'chef_url': reverse('chef_list')})

def chef_detail(request, slug):
    chef = get_object_or_404(ChefProfile, slug=slug)
    recipes = Recipe.objects.filter(chef=chef)
    return render(request, 'chefs/chef_detail.html', {'chef': chef, 'recipes': recipes})