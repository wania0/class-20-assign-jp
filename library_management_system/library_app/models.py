from django.db import models

class Authors(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=500, blank=True)

class Genres(models.Model):
    name = models.CharField(max_length=200)
    
class Books(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author_id = models.IntegerField(null=True, blank=True)
    genre_id = models.IntegerField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)