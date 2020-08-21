from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import CreateNewRecipe
from .models import Recipe, Ingredients
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.forms.models import inlineformset_factory
IngredientFormset = inlineformset_factory(
    Recipe, Ingredients, fields=('name', 'measurement_size', 'measurement_type',)
)

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
    fields = ['name', 'author', 'instructions', 'serving_size']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormset(self.request.POST)
        else:
            data['ingredients'] = IngredientFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        self.object = form.save()
        if ingredients.is_valid():
            ingredients.instance = self.object
            ingredients.save()
        return super().form_valid(form)


    success_url = reverse_lazy('recipes_list')

class RecipesUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'author', 'instructions', 'serving_size']

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered.
        # the difference with CreateView is that
        # on this view we pass instance argument
        # to the formset because we already have
        # the instance created
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["ingredients"] = IngredientFormset(self.request.POST, instance=self.object)
        else:
            data["ingredients"] = IngredientFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context["ingredients"]
        self.object = form.save()
        if ingredients.is_valid():
            ingredients.instance = self.object
            ingredients.save()
        return super().form_valid(form)


    success_url = reverse_lazy('recipes_list')

class RecipesDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes_list')