from pydoc import describe
from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()

    def __str__(self):
        return self.title
class Form(models.Model):
    title=models.CharField(max_length=120)
    def __str__(self):
        return self.title
