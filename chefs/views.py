from django.shortcuts import render, get_object_or_404
from .models import Chef

# Create your views here.
def chef_list(request):
    chefs = Chef.objects.all()
    return render(request, 'chefs/chef_list.html', {'chefs': chefs})

def chef_detail(request, slug):
    chef = get_object_or_404(Chef, slug=slug)
    return render(request, 'chefs/chef_detail.html', {'chef': chef})