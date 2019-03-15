from django.shortcuts import render
from django.views import View
from api.models import IngredientsType


class IndexView(View):

    def get(self, request):
        types = IngredientsType.objects.all()
        return render(request, "index.html", {"types": types})
