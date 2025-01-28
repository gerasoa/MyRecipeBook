from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Recipe

# def my_recipes(request):
#     return HttpResponse("Hello, My recipe!!")


# def under_construction(request):
#     return render(request, 'under_construction.html')


# from django.shortcuts import render
# from django.views.generic import TemplateView


# # Create your views here.
class RecipeList(generic.ListView):
    #model = Recipe
    queryset = Recipe.objects.filter(status=1)
    # template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipe_list'
    template_name = "recipes/index.html"
    paginate_by = 6

   
   

# class HomePage(TemplateView):
#     """
#     Displays home page"
#     """
#     template_name = 'index.html'
