from django.db import models

# Create your models here.

class BooksModel(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    author = models.CharField(max_length=100)
    price = models.IntegerField()