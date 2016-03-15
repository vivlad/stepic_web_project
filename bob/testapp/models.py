from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    rating = models.IntegerField()
    name = models.CharField(max_length=50)

class Article(models.Model):
    author = models.ForeignKey(Author)
    text = models.TextField()