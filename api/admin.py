from django.contrib import admin
from api.models import Ingredient, Recipe, Category, IngredientsType

# Register your models here.
class RecipeAdmin (admin.ModelAdmin):
    list_display = ("name", "link", "added",)

class IngredientAdmin (admin.ModelAdmin):
    list_display = ("name", "type",)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientsType)
