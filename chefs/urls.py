from django.urls import path
from . import views

urlpatterns = [
    path('', views.chef_list, name='chef_list'),
    path('<slug:slug>/', views.chef_detail, name='chef_detail'),
]