from django.shortcuts import render
from api.serializers import RecipeSerializer, CategorySerializer, IngredientSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Recipe, Category, Ingredient

class RecipesView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("category",)

class RecipesItemView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientsView(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

