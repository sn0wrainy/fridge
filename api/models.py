from django.db import models


class IngredientsType(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


class Ingredient(models.Model):

    name = models.CharField(max_length=64, unique=True)
    type = models.ForeignKey(IngredientsType, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


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
