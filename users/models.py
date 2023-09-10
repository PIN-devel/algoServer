from django.db import models


class User(models.Model):
    name = models.CharField(max_length=5)
    baekjoon_id = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
