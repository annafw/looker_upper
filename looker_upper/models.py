from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=100)

    def __str__(self):
        return self.ingredient_name