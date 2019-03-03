from django.db import models

class Ingredient(models.Model):

    VEGETABLES = 0
    FRUITS = 1
    GRAINS = 2
    DAIRY = 3
    SWEETENERS = 4
    SPICES = 5
    OILS = 6
    LEGUMES = 7
    NUTS = 8
    ALCOHOL = 9

    INGREDIENT_TYPE = (
        (VEGETABLES, "warzywa"),
        (FRUITS, "owoce"),
        (GRAINS, "zboża"),
        (DAIRY, "alternatywy nabiału"),
        (SWEETENERS, "słodziki"),
        (SPICES, "przyprawy"),
        (OILS, "tłuszcze"),
        (LEGUMES, "strączki"),
        (NUTS, "orzechy"),
        (ALCOHOL, "alkohol")
    )

    name = models.CharField(max_length=64, unique=True)
    type = models.IntegerField(choices=INGREDIENT_TYPE)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ManyToManyField(Category)
    added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
