from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment, Rating
# from chefs.models import ChefProfile
from .forms import CommentForm
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
# from django.urls import reverse
from django.db.models import Q
from .forms import RatingForm
from django.db.models import Avg
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


def under_construction(request):
    """
    Render the 'Under Construction' placeholder page.

    Args:
        request (HttpRequest): The incoming request.

    Returns:
        HttpResponse: The rendered 'under_construction' template.
    """
    return render(request, 'under_construction.html')


class RecipeList(generic.ListView):
    """
    Display a list of the latest published recipes on the homepage.

    Also provides recent recipes, highest rated recipes,
    and (if authenticated) the user's favourite recipes in context.
    """

    model = Recipe
    context_object_name = 'recipe_list'
    template_name = "recipes/index.html"

    def get_queryset(self):
        """
        Retrieve the four most recent published recipes.

        Returns:
            QuerySet: A list of Recipe objects.
        """

        return (
            Recipe.objects.filter(status=1)
            .annotate(comment_count=Count('comments'))
            .order_by('-created_on')[:4]
        )

    def get_context_data(self, **kwargs):
        """
        Add additional context to the homepage view.

        Includes recent recipes, highest rated recipes, and
        favourite recipes if the user is authenticated.

        Returns:
            dict: Context data for rendering the template.
        """

        context = super().get_context_data(**kwargs)
        context['recent_recipes'] = (
            Recipe.objects.annotate(comment_count=Count('comments'))
            .order_by('-created_on')[:4]
        )

        context['highest_rated_recipes'] = (
            Recipe.objects
            .annotate(comment_count=Count('comments'))
            .annotate(avg_rating=Avg('ratings__score'))
            .order_by('avg_rating')[:4]
        )

        if self.request.user.is_authenticated:
            context['favorite_recipes'] = (
                self.request.user.favorite_recipes
                .annotate(comment_count=Count('comments'))[:4]
            )
        else:
            context['favorite_recipes'] = Recipe.objects.none()
        return context


def Recipe_detail(request, slug):
    """
    Display a specific recipe in detail, along with its comments and
    rating form.

    Handles both GET and POST:
    - GET: Shows the recipe and empty forms.
    - POST: Handles submission of new comments or ratings.

    Args:
        request (HttpRequest): The incoming request.
        slug (str): The recipe's slug identifier.

    Returns:
        HttpResponse: The rendered recipe detail page.
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        if 'score' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating, created = Rating.objects.update_or_create(
                    recipe=recipe,
                    user=request.user,
                    defaults={'score': rating_form.cleaned_data['score']}
                )
                recipe.average_rating = recipe.ratings.aggregate(
                    Avg('score')
                )['score__avg']
                recipe.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Rating submitted successfully'
                )
                return redirect('recipe_detail', slug=recipe.slug)
        else:
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
                return redirect('recipe_detail', slug=recipe.slug)
    else:
        rating_form = RatingForm()
        comment_form = CommentForm()

    return render(
        request,
        "recipes/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "rating_form": rating_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Allow the user to edit their own comment on a recipe.

    Args:
        request (HttpRequest): The incoming request.
        slug (str): The slug of the related recipe.
        comment_id (int): The ID of the comment to edit.

    Returns:
        HttpResponseRedirect: Redirect to the recipe detail page.
    """

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
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Allow the user to delete their own comment.

    Args:
        request (HttpRequest): The incoming request.
        slug (str): The slug of the related recipe.
        comment_id (int): The ID of the comment to delete.

    Returns:
        HttpResponseRedirect: Redirect to the recipe detail page.
    """

    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def toggle_favorite(request, recipe_id):
    """
    Toggle a recipe as favourite or remove it from the user's favourites.

    Args:
        request (HttpRequest): The request from a logged-in user.
        recipe_id (int): ID of the recipe being favourited or unfavourited.

    Returns:
        JsonResponse: Contains the updated favourite status.
    """

    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
        is_favorite = False
    else:
        recipe.favorites.add(request.user)
        is_favorite = True
    return JsonResponse({'is_favorite': is_favorite})


class FavoriteRecipesView(LoginRequiredMixin, ListView):
    """
    Display a paginated list of the user's favourite recipes.

    Only accessible to authenticated users.
    """

    model = Recipe
    template_name = 'recipes/favorite_recipes.html'
    context_object_name = 'favorite_recipes'
    paginate_by = 8

    def get_queryset(self):
        return (
            self.request.user.favorite_recipes.all()
            .annotate(comment_count=Count('comments'))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorite_url'] = reverse('favorite_recipes')
        return context


def search_recipes(request):
    """
    Perform a search query on recipe titles, descriptions, or ingredients.

    Args:
        request (HttpRequest): The search request with query parameter.

    Returns:
        HttpResponse: The rendered search results page with matched recipes.
    """

    query = request.GET.get('q')
    if query:
        results = Recipe.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__icontains=query)
        ).annotate(comment_count=Count('comments'))
    else:
        results = Recipe.objects.none()
    return render(
        request,
        'recipes/search_results.html',
        {'results': results, 'query': query}
    )
