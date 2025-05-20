from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.chef_list, name='chef_list'),
    path('<slug:slug>/', views.chef_detail, name='chef_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
