from django.db import models
    
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    movies = models.ManyToManyField(Movie,related_name="actors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


