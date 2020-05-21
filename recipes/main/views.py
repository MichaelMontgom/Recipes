from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import CreateNewRecipe
from .models import Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

# def index(response):
#     return render(response, 'main/home.html')


# def home(response):
#
#     recipes = Recipe.objects.all()
#
#     return render(response, "main/home.html", {'recipes': recipes})
#
#
# def create(response):
#     if response.method == 'POST':
#         form = CreateNewRecipe(response.POST)
#
#         if form.is_valid():
#             n = form.cleaned_data['name']
#             a = form.cleaned_data['author']
#             instructions = form.cleaned_data['instructions']
#             serving_size = form.cleaned_data['serving_size']
#
#             r = Recipe(name=n, author=a, instructions=instructions, serving_size=serving_size)
#             r.save()
#             return redirect('/home')
#     else:
#         form = CreateNewRecipe()
#     return render(response, 'main/create.html', {'form': form})

class RecipesList(ListView):
    model = Recipe

class RecipesView(DetailView):
    model = Recipe

class RecipesCreate(CreateView):
    model = Recipe
    fields = ['name', 'author', 'ingredients', 'instructions', 'serving_size']
    success_url = reverse_lazy('recipes_list')

class RecipesUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'author', 'ingredients', 'instructions', 'serving_size']
    success_url = reverse_lazy('recipes_list')

class RecipesDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes_list')