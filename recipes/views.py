from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import Recipe
from chefs.models import Chef
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chefs'] = Chef.objects.all()
        return context

    def get_queryset(self):
        return Recipe.objects.filter(status=1).order_by('-created_on')
    

def Recipe_detail(request, slug):
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe},
    )
   

# class HomePage(TemplateView):
#     """
#     Displays home page"
#     """
#     template_name = 'index.html'
