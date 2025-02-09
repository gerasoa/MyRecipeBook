from . import views
from django.urls import path
from .views import RecipeList, Recipe_detail, toggle_favorite,FavoriteRecipesView, search_recipes

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe/<slug:slug>/', views.Recipe_detail, name='recipe_detail'),
    path('favorites/', FavoriteRecipesView.as_view(), name='favorite_recipes'),
    path('search/', search_recipes, name='search_recipes'),
    path('<slug:slug>/', views.Recipe_detail, name='recipe_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('toggle_favorite/<int:recipe_id>/', toggle_favorite, name='toggle_favorite'),     
    
]