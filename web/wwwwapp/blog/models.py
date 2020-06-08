from django.db import models

# Create your models here.

class Post(models.Model):
    # pola klasowe, nie ma inita:
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True) #budowa linku do posta
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) #bedzie sie data automatycznie updatowala
    updated_at = models.DateTimeField(auto_now=True)
