from django.db import models

from problems.models import Problem
from users.models import User


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='leading_groups')
    members = models.ManyToManyField(User, related_name='joined_groups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Round(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    problems = models.ManyToManyField(Problem, blank=True)
    participants = models.ManyToManyField(User, blank=True, related_name='participated_rounds')
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
