from django.shortcuts import render
from django.views import View
from api.models import Ingredient


class IndexView(View):

    def get(self, request):
        ingredients = Ingredient.objects.all()
        return render(request, "index.html", {"ingredients": ingredients})
