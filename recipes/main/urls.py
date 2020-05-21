from django.urls import path

from . import views

urlpatterns = [
    path('', views.RecipesList.as_view(), name='recipes_list'),
    path("view/<int:pk>", views.RecipesView.as_view(), name="recipes_view"),
    path('new', views.RecipesCreate.as_view(), name='recipes_new'),
    path('view/<int:pk>', views.RecipesView.as_view(), name='recipes_view'),
    path('edit/<int:pk>', views.RecipesUpdate.as_view(), name='recipes_edit'),
    path('delete/<int:pk>', views.RecipesDelete.as_view(), name='recipes_delete')



]