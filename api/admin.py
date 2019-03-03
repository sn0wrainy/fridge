from django.contrib import admin
from api.models import Ingredient, Recipe, Category

# Register your models here.
class RecipeAdmin (admin.ModelAdmin):
    list_display = ("name", "link", "added",)

admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
