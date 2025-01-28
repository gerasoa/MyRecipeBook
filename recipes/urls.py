from . import views
from django.urls import path

urlpatterns = [
    # path('', 
    #     views.HomePage.as_view(), name='home'),
    #path('', views.RecipeList.as_view(), name='home'),
    #path('recipes_list.html', views.RecipeList, name='recipe_list'),  # Adicione esta linha
    path('', views.RecipeList.as_view(), name='home'),  # Use a view baseada em classe
]
