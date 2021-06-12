from django.db import models
from django.db.models.base import Model

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
  content = models.CharField(max_length=30)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
