from django.db import models

# Create your models here.


class Ingredients(models.Model):
    name = models.CharField( max_length=100)
    measurement_size = models.FloatField()
    measurement_type = models.CharField(max_length=20)
    
    
    def __str__(self):
        return f'{measurement_size} {measurement_type} {name}'



class Recipe(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredients)
    instructions = models.TextField()
    serving_size = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

