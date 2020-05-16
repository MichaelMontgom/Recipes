from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    instructions = models.TextField()
    serving_size = models.IntegerField()


    def __str__(self):
        return self.name

class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField( max_length=100)
    measurement_size = models.FloatField()
    measurement_type = models.CharField(max_length=20)
    
    
    def __str__(self):
        return f'{measurement_size} {measurement_type} {name}'
