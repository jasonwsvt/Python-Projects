from html import unescape
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Recipe
from .forms import RecipeForm
import requests
import xml.etree.ElementTree as ET

def Recipes_home(request):
    recipes = Recipe.objects.all()
    return render(request, 'Recipes/home.html', {'Recipes': recipes})


def Recipes_get(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.Ingredients = unescape(recipe.Ingredients)
    recipe.Instructions = unescape(recipe.Instructions)
    return render(request, 'Recipes/get.html', {'b': recipe})


def Recipes_create(request):
    form = RecipeForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = form.save()
        return redirect('Recipes_get', pk=result.id)
    else:
        return render(request, 'Recipes/create.html', {'form': form})


def Recipes_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, instance=recipe)
    if request.POST and form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return render(request, 'Recipes/get.html', {'b': recipe})
    else:
        context = {'form': form,
                   'id': recipe.pk,
                   'error': 'The form was not updated successfully. Please enter valid information.'}
        return render(request, 'Recipes/edit.html', context)


def Recipes_delete(request, pk):
    Recipe.objects.filter(id=pk).delete()
    recipes = Recipe.objects.all()
    return render(request, 'Recipes/home.html', {'Recipes': recipes})


def Recipes_favorite(request, pk):
    if request.method == "POST":
        pk = request.POST.get("id")
        recipe = Recipe.objects.get(id=pk)
        recipe.Favorite = not recipe.Favorite
        recipe.save()
        data = { "msg": "Favorite toggled.", 'value': recipe.Favorite, 'id': pk, }
        return JsonResponse(data)
