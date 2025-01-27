from django.shortcuts import render
from django.http import HttpResponse


def my_recipes(request):
    return HttpResponse("Hello, My recipe!!")


def under_construction(request):
    return render(request, 'under_construction.html')


# from django.shortcuts import render
# from django.views.generic import TemplateView


# # Create your views here.
# class HomePage(TemplateView):
#     """
#     Displays home page"
#     """
#     template_name = 'index.html'
