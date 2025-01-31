from django.shortcuts import render, get_object_or_404, reverse
# from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from chefs.models import ChefProfile 
from .forms import CommentForm
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required

def under_construction(request):
    return render(request, 'under_construction.html')

# # Create your views here.
class RecipeList(generic.ListView):
    model = Recipe
    context_object_name = 'recipe_list'
    template_name = "recipes/index_1.html"
    
    def get_queryset(self):
        return Recipe.objects.filter(status=1).annotate(comment_count=Count('comments')).order_by('-created_on')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_recipes'] = Recipe.objects.annotate(comment_count=Count('comments')).order_by('-created_on')[:4]
        if self.request.user.is_authenticated:
            context['favorite_recipes'] = self.request.user.favorite_recipes.annotate(comment_count=Count('comments'))
        else:
            context['favorite_recipes'] = Recipe.objects.none()
        return context
    
  

def Recipe_detail(request, slug):
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
    comment_form = CommentForm()
    return render(
        request,
        "recipes/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):

    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):

    queryset = Recipe.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def toggle_favorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
        is_favorite = False
    else:
        recipe.favorites.add(request.user)
        is_favorite = True
    return JsonResponse({'is_favorite': is_favorite})
