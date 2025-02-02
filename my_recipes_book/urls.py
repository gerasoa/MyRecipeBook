"""
URL configuration for my_recipes_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from recipes import views as recipes
from recipes import views as recipes_views


urlpatterns = [
    # path('', recipes.my_recipes, name='home'),  # Define a URL raiz como a view my_recipes
    # path('', recipes.under_construction, name='under_construction'),
    # path('recipes/', recipes.my_recipes, name='recipes'), 
    # path('summernote/', include('django_summernote.urls')),    
    #path("", include("recipes.urls"), name="recipes-urls"),
    # path('about/', include('about.urls')),
    # path('admin/', admin.site.urls),
    # path('', include('recipes.urls'), name='home'),      
    # path('chefs/', include('chefs.urls')),
    # path("accounts/", include("allauth.urls")),

    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('chefs/', include('chefs.urls')),
    path('about/', include('about.urls')),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')), 
    # Remova ou comente a linha abaixo que aponta para under_construction
    # path('', views.under_construction, name='under_construction'),
    # Adicione a linha abaixo para apontar para a view RecipeList
    path('', recipes_views.RecipeList.as_view(), name='home'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
