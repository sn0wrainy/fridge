from api.serializers import RecipeSerializer, CategorySerializer, IngredientSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Recipe, Category, Ingredient
from django_filters import rest_framework as filters


class AvailableIngredientsFilter(filters.Filter):
    def filter(self, qs, value):
        if not value:
            return Recipe.objects.none()

        available = value.split(",")
        missing = Ingredient.objects.exclude(id__in = available)

        return qs.exclude(ingredients__in = missing)

class RecipesFilter(filters.FilterSet):
    ingredients = AvailableIngredientsFilter("ingredients")

    class Meta:
        model = Recipe
        fields = ["category"]


class RecipesView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipesFilter

class RecipesItemView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientsView(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

