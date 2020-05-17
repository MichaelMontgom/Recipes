from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewRecipe
from .models import Recipe, Ingredients
from django.views.generic import ListView, DetailView
# Create your views here.

def index(response):
    return render(response, 'main/home.html')


def create(response):
    if response.method == 'POST':
        form = CreateNewRecipe(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            a = form.cleaned_data['author']
            instructions = form.cleaned_data['instructions']
            serving_size = form.cleaned_data['serving_size']

            r = Recipe(name=n, author=a, instructions=instructions, serving_size=serving_size)
            r.save()
            return HttpResponseRedirect('%i' %r.id)
    else:
        form = CreateNewRecipe()
    return render(response, 'main/create.html', {'form': form})



