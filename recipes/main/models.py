from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    # ingredients = models.TextField()
    instructions = models.TextField()
    serving_size = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField( max_length=100)
    measurement_size = models.FloatField()
    measurement_type = models.CharField(max_length=20)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.measurement_size} {self.measurement_type} {self.name}'