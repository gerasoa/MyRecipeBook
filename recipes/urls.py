from . import views
from django.urls import path

urlpatterns = [
    # path('', 
    #     views.HomePage.as_view(), name='home'),
    #path('', views.RecipeList.as_view(), name='home'),
    #path('recipes_list.html', views.RecipeList, name='recipe_list'),
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.Recipe_detail, name='recipe_detail'),
     path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
