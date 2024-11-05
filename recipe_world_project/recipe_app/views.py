from django.shortcuts import render

from django.views import generic

from .models import Recipe

class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

    

# Create your views here.
